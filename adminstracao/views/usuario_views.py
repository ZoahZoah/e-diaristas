from ..forms.usuario_forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})   

def listar_usuario(request):
    User = get_user_model()
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuario.html', {'usuarios': usuarios} )