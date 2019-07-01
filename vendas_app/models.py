from django.db import models
from cliente_app import Cliente
from produto_app import Produto


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, verbose_name='Lista de Produtos')
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
