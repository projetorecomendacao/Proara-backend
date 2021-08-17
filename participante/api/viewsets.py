from rest_framework.response import Response

from participante.models import MaritalStatus,Schooling,Activities, Religion, \
     Ethnicitis, Incapacitis, Gender, Gadgets, InternetAccess, Income, HomeSituation, \
     BiggerIncome, Participant

from participante.api.serializers import MaritalStatusSerializer,SchoolingSerializer, \
     ActivitiesSerializer, ReligionSerializer, EthnicitisSerializer, IncapacitisSerializer, \
     GenderSerializer, GadgetsSerializer, InternetAccessSerializer, IncomeSerializer, HomeSituationSerializer, \
     BiggerIncomeSerializer, ParticipantSerializer

from utils.api.serializer import CustomModelViewSet, IsUser

class MaritalStatusViewSet(CustomModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = MaritalStatus.objects.all()
        if not volta.exists():
            MaritalStatus.objects.create(description = 'Casado(a)')
            MaritalStatus.objects.create(description = 'Solteiro(a)')
            MaritalStatus.objects.create(description = 'Divorciado(a)')
            volta = MaritalStatus.objects.all()            
        dados = MaritalStatusSerializer(volta,many=True)
        return Response(dados.data)


class SchoolingViewSet(CustomModelViewSet):
    queryset = Schooling.objects.all()
    serializer_class = SchoolingSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Schooling.objects.all()
        if not volta.exists():
            Schooling.objects.create(description = 'Não frequentou a escola')
            Schooling.objects.create(description = 'Ensino Fundamental Incompleto')
            Schooling.objects.create(description = 'Ensino Fundamental Completo')
            Schooling.objects.create(description = 'Ensino Médio Incompleto')
            Schooling.objects.create(description = 'Ensino Médio Completo')
            Schooling.objects.create(description = 'Ensino Superior Incompleto')
            Schooling.objects.create(description = 'Ensino Superior Completo')
            Schooling.objects.create(description = 'Prefiro Não Declarar')
            volta = Schooling.objects.all()            
        dados = SchoolingSerializer(volta,many=True)
        return Response(dados.data)


class ActivitiesViewSet(CustomModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Activities.objects.all()
        if not volta.exists():
            Activities.objects.create(description = 'Futebol/Futsal')
            Activities.objects.create(description = 'Voleibol')
            Activities.objects.create(description = 'Capoeira')
            Activities.objects.create(description = 'Skate')
            Activities.objects.create(description = 'Hip Hop')
            Activities.objects.create(description = 'Teatro')
            Activities.objects.create(description = 'Recreação Infantil')
            Activities.objects.create(description = 'Cicuíto')
            Activities.objects.create(description = 'Power Dance')
            Activities.objects.create(description = 'Jiu-Jitsu')
            Activities.objects.create(description = 'Apoio Pedagógico')
            Activities.objects.create(description = 'Retirada de Cesta Básica')
            volta = Activities.objects.all()            
 
        dados = ActivitiesSerializer(volta,many=True)
        return Response(dados.data)



class ReligionViewSet(CustomModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Religion.objects.all()
        if not volta.exists():
            Religion.objects.create(description = 'Católico')
            Religion.objects.create(description = 'Espirita')
            Religion.objects.create(description = 'Agnóstico')
            Religion.objects.create(description = 'Prefiro não declarar')
            volta = Religion.objects.all()            
        dados = ReligionSerializer(volta,many=True)
        return Response(dados.data)


class EthnicitisViewSet(CustomModelViewSet):
    queryset = Ethnicitis.objects.all()
    serializer_class = EthnicitisSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Ethnicitis.objects.all()
        if not volta.exists():
            Ethnicitis.objects.create(description = 'Branca')
            Ethnicitis.objects.create(description = 'Preta')
            Ethnicitis.objects.create(description = 'Parda')
            Ethnicitis.objects.create(description = 'Indígena')
            Ethnicitis.objects.create(description = 'Amarela')
            Ethnicitis.objects.create(description = 'Prefiro Não Declarar')

            volta = Ethnicitis.objects.all()            
        dados = EthnicitisSerializer(volta,many=True)
        return Response(dados.data)


class IncapacitisViewSet(CustomModelViewSet):
    queryset = Incapacitis.objects.all()
    serializer_class = IncapacitisSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Incapacitis.objects.all()
        if not volta.exists():
            Incapacitis.objects.create(description = 'Não')
            Incapacitis.objects.create(description = 'Sim, deficiência física')
            Incapacitis.objects.create(description = 'Sim, deficiência intelectual')
            Incapacitis.objects.create(description = 'Sim, deficiência visual')
            Incapacitis.objects.create(description = 'Sim, deficiência auditiva')
            Incapacitis.objects.create(description = 'Prefiro Não Declarar')

            volta = Incapacitis.objects.all()            
        dados = IncapacitisSerializer(volta,many=True)
        return Response(dados.data)


class GenderViewSet(CustomModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Gender.objects.all()
        if not volta.exists():
            Gender.objects.create(description = 'Masculino')
            Gender.objects.create(description = 'Feminino')
            Gender.objects.create(description = 'Prefiro Não Declarar')
            volta = Gender.objects.all()            

        dados = GenderSerializer(volta,many=True)
        return Response(dados.data)


class GadgetsViewSet(CustomModelViewSet):
    queryset = Gadgets.objects.all()
    serializer_class = GadgetsSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Gadgets.objects.all()
        if not volta.exists():
            Gadgets.objects.create(description = 'Celular Próprio')
            Gadgets.objects.create(description = 'Celular Esmprestado')
            Gadgets.objects.create(description = 'Computador/Notebook Próprio')
            Gadgets.objects.create(description = 'Computador/Notebook Emprestado')
            Gadgets.objects.create(description = 'Não possuo nenhum aparelho para ver as aulas')
            volta = Gadgets.objects.all()            

        dados = GadgetsSerializer(volta,many=True)
        return Response(dados.data)


class InternetAccessViewSet(CustomModelViewSet):
    queryset = InternetAccess.objects.all()
    serializer_class = InternetAccessSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = InternetAccess.objects.all()
        if not volta.exists():
            InternetAccess.objects.create(description = 'Utilizo internet fixa em casa (Wifi, rede cabeada, via rádio, outros)')
            InternetAccess.objects.create(description = 'Utilizo dados móveis (3G, 4G, outras)')
            InternetAccess.objects.create(description = 'Não possuo acesso à internet')
            volta = InternetAccess.objects.all()            

        dados = InternetAccessSerializer(volta,many=True)
        return Response(dados.data)




class IncomeViewSet(CustomModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = Income.objects.all()
        if not volta.exists():
            Income.objects.create(description = 'Maior que R$ 11.000,00')
            Income.objects.create(description = 'Entre R$ 7.700,00 e R$ 11.000,00')
            Income.objects.create(description = 'Entre R$ 4.400,00 e R$ 7.700,00')
            Income.objects.create(description = 'Entre R$ 3.300,00 e R$ 4.400,00')
            Income.objects.create(description = 'Entre R$ 2.200,00 e R$ 3.300,00')
            Income.objects.create(description = 'Entre R$ 1.650,00 e R$ 2.200,00')
            Income.objects.create(description = 'Entre R$ 1.100,00 e R$ 1.650,00')
            Income.objects.create(description = 'Entre R$ 550,00 e R$ 1.100,00')
            Income.objects.create(description = 'Menor que R$ 550,00')
            Income.objects.create(description = 'Prefiro não declarar')
            volta = Income.objects.all()            

        dados = IncomeSerializer(volta,many=True)
        return Response(dados.data)


class HomeSituationViewSet(CustomModelViewSet):
    queryset = HomeSituation.objects.all()
    serializer_class = HomeSituationSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = HomeSituation.objects.all()
        if not volta.exists():
            HomeSituation.objects.create(description = 'Própria')
            HomeSituation.objects.create(description = 'Financiada (pagando)')
            HomeSituation.objects.create(description = 'Alugada')
            HomeSituation.objects.create(description = 'Ocupação')
            HomeSituation.objects.create(description = 'Prefiro não declarar')
            volta = HomeSituation.objects.all()            

        dados = HomeSituationSerializer(volta,many=True)
        return Response(dados.data)


class BiggerIncomeViewSet(CustomModelViewSet):
    queryset = BiggerIncome.objects.all()
    serializer_class = BiggerIncomeSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

    def list(self, request):
        volta = BiggerIncome.objects.all()
        if not volta.exists():
            BiggerIncome.objects.create(description = 'Auxílio e pensões(apos., aux. desem., INSS, Bolsa Fam. ou outros')
            BiggerIncome.objects.create(description = 'Emprego de Carteira Assinada (CLT)')
            BiggerIncome.objects.create(description = 'Emprego Autônomo')
            BiggerIncome.objects.create(description = 'Emprego freelance/temporário/pontual')
            BiggerIncome.objects.create(description = 'Prefiro não declarar')
            volta = BiggerIncome.objects.all()            

        dados = BiggerIncomeSerializer(volta,many=True)
        return Response(dados.data)

class ParticipantViewSet(CustomModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'partial_update': [IsUser],
        'destroy': [IsUser],
        'update': [IsUser]
    }

