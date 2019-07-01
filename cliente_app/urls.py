from django.contrib import path
from .views import cadastro

app_name = 'cliente'

urlpatterns = [
    path('cadastro/', cadastro, name='cliente_cadastro'),
#   path('')
]