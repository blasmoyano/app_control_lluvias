from django.test import TestCase
from .models import LLuvia
from datetime import datetime
from campos.models import Campo
from rest_framework.test import APIClient
from rest_framework import status


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

    def test_lluvia_create(self):
        test = LLuvia.objects.get(lluvia_milimetros=12)
        self.assertTrue(isinstance(test, LLuvia))
        self.assertEqual(test.__str__(), "test_model")


class LluviaApiTestCase(TestCase):
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

    def test_api_promedio(self):
        client = APIClient()
        response = client.get(
            'http://localhost:8080/desarrollo/lluvia/api/v1/promedio?dias=4'
        )
        resultado = response.json()
        self.assertEqual(
            resultado[0].get('test_model'),
            12
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_api_promedio_fail(self):
        client = APIClient()
        response = client.get(
            'http://localhost:8080/desarrollo/lluvia/api/v1/promedio?das=4'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_api_acumulado(self):
        client = APIClient()
        response = client.get(
            'http://localhost:8080/desarrollo/lluvia/api/v1/acumulado?milimetros=4'
        )
        resultado = response.json()

        self.assertEqual(
            resultado[0].get('test_model'),
            12
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_api_acumulado_fail(self):
        client = APIClient()
        response = client.get(
            'http://localhost:8080/desarrollo/lluvia/api/v1/acumulado?sarasa=4'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_api_crear_lluvia(self):
        client = APIClient()
        response = client.post(
            'http://localhost:8080/desarrollo/lluvia/api/v1/crear_lluvia_campo/1',
            data={
                'lluvia_milimetros': 15,
                "lluvia_fecha": datetime.now()
            }
        )
        import pdb; pdb.set_trace()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_api_obtener_info(self):
        client = APIClient()
        response = client.get(
            'http://localhost:8080/desarrollo/lluvia/api/v1/crear_lluvia_campo/1'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
