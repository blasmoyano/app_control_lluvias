from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostLLuviaPorCampo, GetLLuviaPorCampo
from .models import LLuvia
from statistics import mean
from datetime import datetime, timedelta


class CrearLLuviaPorCampo(generics.ListCreateAPIView):
    """
    API: APP Control Lluvia
    Creación de lluvia por campo
    """
    serializer_class = GetLLuviaPorCampo
    lookup_url_kwarg = "lluvia_campo"
    http_method_names = ['post', 'get']

    def get_queryset(self):
        campo_id = self.kwargs.get(self.lookup_url_kwarg)
        return LLuvia.objects.filter(
            lluvia_campo=campo_id
        )

    def get_object(self):
        qry = self.get_queryset()
        obj = get_object_or_404(qry)
        return obj

    def create(self, request, *args, **kwargs):
        campo_id = self.kwargs.get(self.lookup_url_kwarg)
        request.data._mutable = True
        request.data['lluvia_campo'] = int(campo_id)
        request.data._mutable = False

        serializer = PostLLuviaPorCampo(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                "Se inserto correctamente",
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ListPromedio(APIView):
    """
    API: APP Control Lluvia
    Listado de campos con promedio de los ultimos N dias
    """

    def get(self, request):
        data_dias = request.query_params.get('dias', None)
        fecha_final = datetime.now()
        if data_dias is None:
            raise ValidationError(
                {
                    "mensaje": f"Parametro incorrecto"
                }
            )
        else:
            if int(data_dias) > 7:
                raise ValidationError(
                    {
                        "mensaje": f"El numero seleccionado ({data_dias}) "
                                   f"es demaciado grande.)"
                    }
                )
            else:
                fecha_inicio = fecha_final - timedelta(
                    days=int(data_dias)
                )

                query = LLuvia.objects.filter(
                    lluvia_fecha__range=(fecha_inicio, fecha_final)
                )
                json_data = {}

                for qry in query:
                    key = qry.lluvia_campo.campo_nombre
                    value = qry.lluvia_milimetros

                    if json_data.get(key):
                        json_data[key].append(value)
                    else:
                        json_data[key] = [value]

                for k, v in json_data.items():
                    json_data[k] = mean(v)

                return Response([json_data])


class ListAcumulado(APIView):
    """
    API: APP Control Lluvia
    Listado de campos con lluvia acumulada mayor a N
    """

    def get(self, request):
        data_milimetros = request.query_params.get('milimetros', None)

        if data_milimetros is None:
            raise ValidationError(
                {
                    "mensaje": f"Parametro incorrecto"
                }
            )
        else:
            query = LLuvia.objects.all()
            json_data = {}
            json_acumualdo = {}

            for qry in query:
                key = qry.lluvia_campo.campo_nombre
                value = qry.lluvia_milimetros

                if json_data.get(key):
                    json_data[key].append(value)
                else:
                    json_data[key] = [value]

            for k, v in json_data.items():
                json_data[k] = sum(v)

                try:
                    if json_data[k] > float(data_milimetros):
                        json_acumualdo[k] = json_data[k]
                except:
                    raise ValidationError(
                        {
                            "mensaje": f"Ingreso un numero con coma."
                                       f" Debe ser con punto"
                        }
                    )

            return Response([json_acumualdo])


class LluviaCrear(CreateView):
    template_name = 'lluvias/crear_lluvia.html'
    model = LLuvia
    success_url = reverse_lazy('campo_index')
    fields = [
        'lluvia_campo',
        'lluvia_milimetros',
        'lluvia_fecha'
    ]
