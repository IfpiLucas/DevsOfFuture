from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    rg = models.PositiveIntegerField('RG', max_length=16)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField('Endereço', max_length=255)

    def __str__(self):
        return self.nome

tipos = [['flor', 'Flor'], ['vaso', 'Vaso'], ['planta', 'Planta'], ['muda', 'Muda']]

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=6, choices=tipos)
    preco = models.DecimalField('Preço', max_digits=9, decimal_places=2)
    qtd_estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, verbose_name='Lista de Produtos')
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

objetos = models.Manager()