from django.test import TestCase
from laboratorio.models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio inicial para las pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Central",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_laboratorio_data(self):
        # Obtener el laboratorio creado en setUpTestData
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)

        # Verificar que los datos coincidan
        self.assertEqual(laboratorio.nombre, "Laboratorio Central")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")

    def test_str_method(self):
        # Verificar que el método __str__ devuelva el nombre correctamente
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(str(laboratorio), "Laboratorio Central")