import unittest
from flask import current_app
from app import create_app
import os
from app.models import Facultad

class FacultadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ciencias"
        facultad.abreviatura = "FCC"
        facultad.directorio = "Ciencias"
        facultad.sigla = "FCC"
        facultad.codigoPostal = "12345"
        facultad.ciudad = "Ciudad"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Contacto"
        facultad.email = "test@gmail.com"
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")
        self.assertEqual(facultad.abreviatura, "FCC")
        self.assertEqual(facultad.directorio, "Ciencias")
        self.assertEqual(facultad.sigla, "FCC")
        self.assertEqual(facultad.codigoPostal, "12345")
        self.assertEqual(facultad.ciudad, "Ciudad")
        self.assertEqual(facultad.domicilio, "Calle 123")
        self.assertEqual(facultad.telefono, "123456789")
        self.assertEqual(facultad.contacto, "Contacto")
        self.assertEqual(facultad.email,"test@gmail.com")