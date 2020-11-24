"""app_control_lluvias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Alarmas API",
        default_version='v1',
        description="Documentacion de la API de alarmas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        f'{settings.URL_NAME}admin/',
        admin.site.urls
    ),
    path(
        f'{settings.URL_NAME}lluvia/',
        include('lluvias.urls')
    ),
    path(
        f'{settings.URL_NAME}campo/',
        include('campos.urls')
    ),
    url(r'^docs/$',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'),
]

admin.site.site_header = "Kilimo"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "Kilimo"
