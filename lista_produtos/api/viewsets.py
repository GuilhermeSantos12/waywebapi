from rest_framework.viewsets import ModelViewSet
from lista_produtos.models import ListaProdutos
from .serializers import ListaProdutosSerializer

class ListaProdutosViewSet(ModelViewSet):
    queryset = ListaProdutos.objects.all()
    serializer_class = ListaProdutosSerializer
