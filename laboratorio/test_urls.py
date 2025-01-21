from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioURLTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio para las pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Central",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_laboratorio_detail_url(self):
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)