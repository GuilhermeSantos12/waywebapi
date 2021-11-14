from django.db import models


# Create your models here.
class ListaCategoria(models.Model):
    foto = models.ImageField(upload_to='Lista_Categoria', null=True, blank=True)
    categorias = models.CharField(max_length=150)
    definicao = models.TextField()

    def __str__(self):
        return self.categorias
