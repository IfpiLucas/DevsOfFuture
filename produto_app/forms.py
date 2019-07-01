from django import forms
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'tipo', 'preco', 'qtd_estoque']