# laboratorio/test_views.py
from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioDetailViewTest(TestCase):
    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Central",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_laboratorio_detail_view(self):
        # Modificar esta línea para incluir el namespace 'laboratorio:'
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)