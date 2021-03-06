# Generated by Django 3.1.3 on 2020-11-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_nombre', models.CharField(max_length=144, verbose_name='Nombre del campo')),
                ('campo_hectarea', models.IntegerField(verbose_name='Cantidad de hectareas')),
                ('campo_latitud', models.FloatField(verbose_name='Latitud')),
                ('campo_longitud', models.FloatField(verbose_name='Longitud')),
                ('campo_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Campo',
                'verbose_name_plural': 'Campos',
                'ordering': ['campo_nombre', '-campo_created'],
            },
        ),
    ]
