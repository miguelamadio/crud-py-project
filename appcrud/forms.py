from django.forms import ModelForm
from appcrud.models import Livros

# Cria a classe de formulário.
class LivrosForm(ModelForm):
     class Meta:
         #o modelo toma como base o metodo LIVROS
         model = Livros
         #define os campos que estarão no formulário
         fields = ["titulo", "autor", "editora", "genero","ano_ed"]
    