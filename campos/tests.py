from django.test import TestCase
from .models import Campo


class CampoTestCase(TestCase):
    def setUp(self):
        Campo.objects.create(
            campo_nombre="test_model",
            campo_hectarea=12,
            campo_latitud=13.3,
            campo_longitud=13
        )

    def test_campo_create(self):
        test = Campo.objects.get(campo_nombre="test_model")
        self.assertTrue(isinstance(test, Campo))
        self.assertEqual(test.__unicode__(), "test_model")
