from utils.api.serializer import CustomModelViewSet, IsUser
from doafumcadmodel.models import Cidade
from doafumcadmodel.api.serializers import CidadeSerializer

class CidadeViewSet (CustomModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }