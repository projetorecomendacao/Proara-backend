from utils.api.serializer import CustomModelViewSet, IsUser
from doafumcadmodel.models import Boleto, Cidade, Instituicao, Patrocinador, Pessoa
from doafumcadmodel.api.serializers import BoletoSerializer, CidadeSerializer, InstituicaoSerializer, PatrocinadorSerializer, PessoaSerializer

class BoletoViewSet (CustomModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

class CidadeViewSet (CustomModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

class PessoaViewSet (CustomModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

class InstituicaoViewSet (CustomModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

class PatrocinadorViewSet (CustomModelViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }