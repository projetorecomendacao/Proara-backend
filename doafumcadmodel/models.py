from django.db import models

class Cidade(models.Model):
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=2, null= True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        ordering = ['id']
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


