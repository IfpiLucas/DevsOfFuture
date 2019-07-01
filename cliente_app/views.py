from django.shortcuts import render
from forms import ClienteForm

def cadastro(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClienteForm()
    return render(request, 'cliente/cadastro.html', {'form': form})
