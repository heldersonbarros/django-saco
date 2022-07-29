from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ClienteList.as_view(), name="home"),
    path('cliente/all', views.ClienteList.as_view(), name="cliente_list"),
    path('cliente/create', views.ClienteCreate.as_view(), name="cliente_create"),
    path('funcionario/all', views.FuncionarioList.as_view(), name="funcionario_list"),
    path('funcionario/create', views.FuncionarioCreate.as_view(), name="funcionario_create"),
    path('funcionario/<int:pessoa_id>/delete', views.FuncionarioDelete.as_view(), name="funcionario_delete"),
    path('ordem_servico/create', views.OrdemServicoCreate.as_view(), name="ordemServico_create"),
    path('ordem_servico/all', views.OrdemServicoList.as_view(), name="ordemServico_list"),
    path('ordem_servico/<int:pk>/update', views.OrdemServicoUpdate.as_view(), name="ordemServico_update"),
    path('calcular_distancia', views.CalcularDistancia.as_view(), name="calcular_distancia"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)