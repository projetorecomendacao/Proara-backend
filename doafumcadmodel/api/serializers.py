from rest_framework import serializers
from doafumcadmodel.models import Cidade

class CidadeSerializer (serializers.ModelSerializer):

        class Meta:
            model = Cidade
            fields = '__all__'