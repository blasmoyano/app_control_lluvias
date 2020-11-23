from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/crear_lluvia_campo/<lluvia_campo>',
        views.CrearLLuviaPorCampo.as_view()
    ),
    path(
        'api/v1/promedio',
        views.ListPromedio.as_view()
    ),
    path(
        'api/v1/acumulado',
        views.ListAcumulado.as_view()
    ),
    ]
