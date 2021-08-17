from django.contrib import admin

# Register your models here.

from participante.models import MaritalStatus,Schooling,Activities, Religion, \
     Ethnicitis, Incapacitis, Gender, Gadgets, InternetAccess, Income, HomeSituation, \
     BiggerIncome, Participant

admin.site.register(MaritalStatus)
admin.site.register(Schooling)
admin.site.register(Activities)
admin.site.register(Religion)
admin.site.register(Ethnicitis)
admin.site.register(Incapacitis)
admin.site.register(Gender)
admin.site.register(Gadgets)
admin.site.register(InternetAccess)
admin.site.register(Income)
admin.site.register(HomeSituation)
admin.site.register(BiggerIncome)
admin.site.register(Participant)
