from rest_framework.serializers import ModelSerializer
from lista_categoria.models import ListaCategoria

class ListaCategoriaSerializer(ModelSerializer):
    class Meta:
        model = ListaCategoria
        fields = ['id', 'foto', 'categorias', 'definicao']
