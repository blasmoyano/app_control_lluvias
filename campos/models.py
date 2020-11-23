from django.db import models


class Campo(models.Model):
    campo_nombre = models.CharField(
        max_length=144,
        verbose_name="Nombre del campo"
    )
    campo_hectarea = models.IntegerField(
        verbose_name="Cantidad de hectáreas"
    )
    campo_latitud = models.FloatField(
        verbose_name="Latitud"
    )
    campo_longitud = models.FloatField(
        verbose_name="Longitud"
    )
    campo_fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )
    campo_fecha_actualizacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Campo"
        verbose_name_plural = "Campos"
        ordering = [
            "campo_nombre",
            "-campo_fecha_creacion"
        ]

    def __str__(self):
        return self.campo_nombre
