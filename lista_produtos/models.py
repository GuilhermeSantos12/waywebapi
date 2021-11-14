from django.db import models
from lista_categoria.models import ListaCategoria

# Create your models here.
class ListaProdutos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='Lista_Produtos', null=True, blank=True)
    categorias = models.ManyToManyField(ListaCategoria)

    def __str__(self):
        return self.nome
