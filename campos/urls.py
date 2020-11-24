from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.CamposIndex.as_view(),
        name="campo_index"
    ),
    path(
        'crear_campo/',
        views.CampoCrear.as_view(),
        name="campo_crear"),

]
