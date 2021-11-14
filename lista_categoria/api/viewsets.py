from rest_framework.viewsets import ModelViewSet
from lista_categoria.models import ListaCategoria
from .serializers import ListaCategoriaSerializer

class ListaCategoriaViewSet(ModelViewSet):

    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ListaCategoria.objects.all()
    serializer_class = ListaCategoriaSerializer