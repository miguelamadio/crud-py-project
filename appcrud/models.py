from django.db import models

# Create your models here.
class Livros(models.Model):
    capa = models.ImageField()
    titulo = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    editora = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    ano_ed = models.IntegerField()
