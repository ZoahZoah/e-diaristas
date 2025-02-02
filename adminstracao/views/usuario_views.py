from ..forms.usuario_forms import CadastroUsuarioForm, EditarUsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_usuario(request):
    is_editing = False
    if request.method == 'POST':
        form_usuario = CadastroUsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_usuarios')
    else:
        form_usuario = CadastroUsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario, 'is_editing':is_editing})   

@login_required
def listar_usuarios(request):
    User = get_user_model()
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuario.html', {'usuarios': usuarios} )

@login_required
def editar_usuario(request, id): 
    User = get_user_model()
    usuario = User.objects.get(id=id)
    form_usuario = EditarUsuarioForm(request.POST or None, instance=usuario)
    is_editing = True
    if form_usuario.is_valid():
        form_usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario, 'is_editing':is_editing})