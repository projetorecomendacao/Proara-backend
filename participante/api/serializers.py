from rest_framework.serializers import ModelSerializer
from participante.models import MaritalStatus,Schooling,Activities, Religion, \
     Ethnicitis, Incapacitis, Gender, Gadgets, InternetAccess, Income, HomeSituation, \
     BiggerIncome, Participant


class MaritalStatusSerializer(ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class SchoolingSerializer(ModelSerializer):
    class Meta:
        model = Schooling
        fields = '__all__'


class ActivitiesSerializer(ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'


class ReligionSerializer(ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'


class EthnicitisSerializer(ModelSerializer):
    class Meta:
        model = Ethnicitis
        fields = '__all__'


class IncapacitisSerializer(ModelSerializer):
    class Meta:
        model = Incapacitis
        fields = '__all__'


class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class GadgetsSerializer(ModelSerializer):
    class Meta:
        model = Gadgets
        fields = '__all__'


class InternetAccessSerializer(ModelSerializer):
    class Meta:
        model = InternetAccess
        fields = '__all__'


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class HomeSituationSerializer(ModelSerializer):
    class Meta:
        model = HomeSituation
        fields = '__all__'


class BiggerIncomeSerializer(ModelSerializer):
    class Meta:
        model = BiggerIncome 
        fields = '__all__'


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'