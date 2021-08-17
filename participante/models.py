from django.db import models
from django.db.models.deletion import DO_NOTHING
from doafumcadmodel.models import Cidade
# Create your models here.

class MaritalStatus (models.Model):
    description = models.CharField(max_length=35)

    class Meta:
        ordering = ['id']


class Schooling(models.Model):
    description = models.CharField(max_length=35)

    class Meta:
        ordering = ['id']


class Activities(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Ethnicitis(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Incapacitis(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']        


class Gender(models.Model):
    description = models.CharField(max_length=35)

    class Meta:
        ordering = ['id']    

class Gadgets(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']    


class InternetAccess(models.Model):
    description = models.CharField(max_length=75)

    class Meta:
        ordering = ['id'] 

class Income(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class HomeSituation (models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Religion(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

class BiggerIncome(models.Model):
    description = models.CharField(max_length=70)

    class Meta:
        ordering = ['id']


class Participant(models.Model):
    p00_email = models.CharField("Email da Google", null=True, blank=True, max_length=80)
    p01_name = models.CharField('Nome:', max_length=50)
    p03_name_social = models.CharField('Nome:', max_length=50, null=True, blank=True)
    #p02_address = models.OneToOneField(AddressPlace, on_delete=models.DO_NOTHING, null=True)
    p03_phone = models.CharField('Meios de Entrar em contato', max_length=14, null=True, blank=True)
    p03_is_whatsapp = models.CharField(default='N', max_length=1)
    p04_birth_date = models.CharField(max_length=10, null=True, blank=True)
    p05_CPF = models.CharField(max_length=14,null=True, blank=True) 
    p05_RG = models.CharField(max_length=14,null=True, blank=True) 
    p05_RG_emissor = models.CharField(max_length=20,null=True, blank=True)
    p05_RG_Estado = models.CharField(max_length=2,null=True, blank=True) 
    p06_gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, null=True, blank=True)
    p07_marital_status = models.ForeignKey(MaritalStatus, on_delete=models.DO_NOTHING, null=True, blank=True)
    P08_is_student = models.CharField(max_length=3, null=True, blank=True) 
    p08_schooling = models.ForeignKey(Schooling, on_delete=models.DO_NOTHING, null=True, blank=True)
    p09_ethnicity = models.ForeignKey(Ethnicitis, on_delete=models.DO_NOTHING, null=True, blank=True)
    p10_incapacity = models.ForeignKey(Incapacitis, on_delete=models.DO_NOTHING, null=True, blank=True)
    p11_gadgets = models.ForeignKey(Gadgets, on_delete=models.DO_NOTHING, null=True, blank=True)
    p12_internet_access = models.ForeignKey(InternetAccess, on_delete=models.DO_NOTHING, null=True, blank=True)
    p13_0_social_information = models.CharField(default='N', max_length=1)
    p13_income_family = models.ForeignKey(Income, on_delete=models.DO_NOTHING, null=True, blank=True)
    p14_lives_with = models.IntegerField(default=0, null=True, blank=True)
    p15_home_situation = models.ForeignKey(HomeSituation, on_delete=models.DO_NOTHING, null=True, blank=True)
    p16_bigger_income = models.ForeignKey(BiggerIncome, on_delete=models.DO_NOTHING, null=True, blank=True)
    p17_responsible_name = models.CharField('Nome:', max_length=50)
    p18_responsible_email = models.CharField(null=True, blank=True, max_length=80)
    p19_responsible_phone = models.CharField(max_length=14, null=True, blank=True)
    p19_same_participante = models.CharField(default='N', max_length=1)
    #p20_profile_photo_URL = models.ImageField(upload_to='profile_photos', null=True)
    p30_public_place = models.CharField(max_length=75, blank=True)     # logradouro
    p31_number_place = models.CharField(max_length=8, blank=True)      #número 
    p32_district = models.CharField(max_length=60, blank=True)         # bairro
    p33_cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, null=True, blank=True)
    p34_cep = models.CharField(max_length=9, blank=True)
    p40_activities = models.ManyToManyField(Activities)

    class Meta:
        ordering = ['id']
