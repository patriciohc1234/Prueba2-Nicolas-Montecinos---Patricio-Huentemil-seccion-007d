from django.test import TestCase
from .models import Catalogo

class CatalogoTestCase(TestCase):

 def test_catalogo(self):
  catalogo1 = Catalogo.objects.get(title="t-shirt") 

