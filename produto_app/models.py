from django.db import models

tipos = [['flor', 'Flor'], ['vaso', 'Vaso'], ['planta', 'Planta'], ['muda', 'Muda']]

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=6, choices=tipos)
    preco = models.DecimalField('Preço', max_digits=9, decimal_places=2)
    qtd_estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome
