from django.urls import path   
from .views import servicos_views, usuario_views

urlpatterns = [
    path('servicos/cadastrar', servicos_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servicos_views.listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', servicos_views.editar_servico, name='editar_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuarios'),
]