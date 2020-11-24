from django.db import models


class LLuvia(models.Model):
    lluvia_milimetros = models.FloatField(
        verbose_name="Milímetros"
    )
    lluvia_fecha = models.DateTimeField(
        verbose_name="Fecha"
    )
    lluvia_campo = models.ForeignKey(
        "campos.Campo",
        verbose_name="Campo",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "LLuvia"
        verbose_name_plural = "LLuvias"
        ordering = [
            "lluvia_fecha",
        ]

    def __str__(self):
        return self.lluvia_campo.campo_nombre
