from django.db import models


# Create your models here.

class Sinal(models.Model):
    configuracao_da_mao = models.CharField(max_length=4, null=False)
    ponto_de_articulacao = models.CharField(max_length=4, null=False)
    movimento = models.CharField(max_length=4, null=False)
    orientacao_das_maos = models.CharField(max_length=4, null=False)
    expressao_facil_corporal = models.CharField(max_length=4, null=False)
    nome = models.CharField(max_length=255, null=False)

    def sinal_url(self):
        return u"/sinais/%i" % self.id

