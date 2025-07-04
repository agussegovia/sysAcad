import unittest
from flask import current_app
from app import create_app
import os
from app.models import Grado, Facultad
class GradoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_grado_creation(self):
        grado = Grado()
        facultad = Facultad()
        
        grado.nombre = "Grado en Matemáticas"
        grado.facultad = facultad
        
        facultad.nombre = "Facultad de Ciencias Exactas"
        
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, "Grado en Matemáticas")
        self.assertIsNotNone(grado.facultad)
        self.assertEqual(grado.facultad.nombre, "Facultad de Ciencias Exactas")
