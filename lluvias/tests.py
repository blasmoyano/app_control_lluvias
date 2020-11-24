from django.test import TestCase
from .models import LLuvia
from datetime import datetime
from campos.models import Campo


class LLuviaTestCase(TestCase):
    def setUp(self):
        Campo.objects.create(
            campo_nombre="test_model",
            campo_hectarea=12,
            campo_latitud=13.3,
            campo_longitud=13
        )
        campo = Campo.objects.get(campo_nombre="test_model")

        LLuvia.objects.create(
            lluvia_milimetros=12,
            lluvia_fecha=datetime.now(),
            lluvia_campo=campo,
        )

    def test_campo_create(self):
        test = LLuvia.objects.get(lluvia_milimetros=12)
        self.assertTrue(isinstance(test, LLuvia))
        self.assertEqual(test.__str__(), "test_model")
