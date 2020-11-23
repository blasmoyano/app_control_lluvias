from django.contrib import admin
from .models import LLuvia


class LLuviaAdmin(admin.ModelAdmin):
    list_display = ('lluvia_campo', 'lluvia_milimetros', 'lluvia_fecha')
    search_fields = ('lluvia_campo__campo_nombre',)
    date_hierarchy = 'lluvia_fecha'
    list_filter = ('lluvia_campo__campo_nombre',)


admin.site.register(LLuvia, LLuviaAdmin)
