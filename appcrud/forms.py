from django.forms import ModelForm
from appcrud.models import Livros

# Create the form class.
class LivrosForm(ModelForm):
     class Meta:
         model = Livros
         fields = ["titulo", "autor", "editora", "genero","ano_ed"]
