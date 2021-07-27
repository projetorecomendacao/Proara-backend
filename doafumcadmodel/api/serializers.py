from rest_framework import serializers
from doafumcadmodel.models import Boleto, Cidade, Pessoa, Instituicao, Patrocinador

class BoletoSerializer (serializers.ModelSerializer):

        class Meta:
            model = Boleto
            fields = '__all__'


class CidadeSerializer (serializers.ModelSerializer):

        class Meta:
            model = Cidade
            fields = '__all__'


class PessoaSerializer (serializers.ModelSerializer):

        class Meta:
            model = Pessoa
            fields = '__all__'


class InstituicaoSerializer (serializers.ModelSerializer):

        class Meta:
            model = Instituicao
            fields = '__all__'
            

class PatrocinadorSerializer (serializers.ModelSerializer):

        class Meta:
            model = Patrocinador
            fields = '__all__'
