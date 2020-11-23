from django.contrib import admin
from .models import Campo


class CampoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'campo_fecha_creacion',
        'campo_fecha_actualizacion'
    )
    list_display = ('campo_nombre', 'campo_hectarea')
    search_fields = ('campo_nombre',)


admin.site.register(Campo, CampoAdmin)
