from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    rg = models.CharField('RG', max_length=16)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField('Endereço', max_length=255)

    def __str__(self):
        return self.nome
