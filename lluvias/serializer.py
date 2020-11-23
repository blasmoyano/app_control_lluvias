from rest_framework import serializers
from .models import LLuvia


class GetLLuviaPorCampo(serializers.ModelSerializer):

    class Meta:
        model = LLuvia
        fields = (
            'lluvia_milimetros',
            'lluvia_fecha',
            'lluvia_campo',
        )
        depth = 1


class PostLLuviaPorCampo(serializers.ModelSerializer):

    class Meta:
        model = LLuvia
        fields = (
            'lluvia_milimetros',
            'lluvia_fecha',
            'lluvia_campo',
        )
