from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Campo


class CamposIndex(ListView):
    model = Campo
    template_name = "campos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CampoCrear(CreateView):
    template_name = 'campos/crear_campo.html'
    model = Campo
    success_url = reverse_lazy('campo_index')
    fields = [
        'campo_nombre',
        'campo_hectarea',
        'campo_latitud',
        'campo_longitud'
    ]
