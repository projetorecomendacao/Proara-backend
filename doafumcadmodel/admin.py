from django.contrib import admin
from doafumcadmodel.models import Boleto, Cidade, Instituicao, Patrocinador, Pessoa

# Register your models here.

admin.site.register(Boleto)
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Pessoa)
admin.site.register(Patrocinador)

