from rest_framework.serializers import ModelSerializer
from lista_produtos.models import ListaProdutos

class ListaProdutosSerializer(ModelSerializer):
    class Meta:
        model = ListaProdutos
        fields = ['id', 'nome', 'descricao', 'foto', 'categorias']