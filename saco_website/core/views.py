from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView, DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from . models import Cliente, Funcionario, OrdemServico, Pessoa, Servico, Veiculo
from . forms import ClienteForm, EnderecoForm, PessoaForm, FuncionarioForm, OrdemServicoForm, VeiculoForm, VerificarDistancia
from django.contrib.messages.views import SuccessMessageMixin


class ClienteCreate(TemplateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "core/cliente_form.html"
    extra_context = {"title": "Adicionar cliente"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pessoa_form"] = PessoaForm(prefix="pessoa_pre")
        context["cliente_form"] = ClienteForm(prefix="cliente_pre")
        context["veiculo_form"] = VeiculoForm(prefix="veiculo_pre")
        context["endereco_form"] = EnderecoForm(prefix="endereco_pre")
        return context

    def post(self, request, *arg, **kwargs):
        pessoa_form = PessoaForm(request.POST, prefix="pessoa_pre")
        cliente_form = ClienteForm(request.POST, prefix="cliente_pre")
        veiculo_form = VeiculoForm(request.POST, prefix="veiculo_pre")
        endereco_form = EnderecoForm(request.POST, prefix="endereco_pre")
        
        if pessoa_form.is_valid() and cliente_form.is_valid():
            pessoa = pessoa_form.save()
            cliente_form.instance.pessoa = pessoa
            cliente = cliente_form.save()
            veiculo_form.instance.cliente = cliente
            veiculo_form.save()
            endereco_form.save()

        return super().render_to_response(self.get_context_data())

class FuncionarioCreate(TemplateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "core/funcionario_form.html"
    extra_context = {"title": "Adicionar Funcionário"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pessoa_form"] = PessoaForm(prefix="pessoa_pre")
        context["funcionario_form"] = FuncionarioForm(prefix="funcionario_pre")
        return context

    def post(self, request, *arg, **kwargs):
        pessoa_form = PessoaForm(request.POST, prefix="pessoa_pre")
        funcionario_form = FuncionarioForm(request.POST, prefix="funcionario_pre")
        
        if pessoa_form.is_valid() and funcionario_form.is_valid():
            pessoa = pessoa_form.save()
            funcionario_form.instance.pessoa = pessoa
            funcionario_form.save()

        return super().render_to_response(self.get_context_data())

class ClienteList(ListView):
    model = Cliente
    extra_context = {"title": "Clientes"}

class FuncionarioList(ListView):
    model = Funcionario
    extra_context = {"title": "Funcionários"}

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("funcionario_list")
    pk_url_kwarg = 'pessoa_id'
    extra_context = {"title": "Deletar Funcionário"}

class OrdemServicoCreate(CreateView):
    model = OrdemServico
    extra_context = {"title": "Adicionar ordem de serviço"}
    form_class = OrdemServicoForm
    template_name = "core/ordemServico_form.html"
    success_url = reverse_lazy("home")

class OrdemServicoList(ListView):
    model = OrdemServico
    extra_context = {"title": "Ordens de serviço"}

    def get_queryset(self):
        atendido = self.request.GET.get("atendido")
        if atendido:
            return self.model.objects.filter(data_conclusao=None)

        return super().get_queryset()

class OrdemServicoUpdate(UpdateView):
    model = OrdemServico
    extra_context = {"title": "Atualizar ordem de serviço"}
    form_class = OrdemServicoForm
    template_name = "core/ordemServico_form.html"
    success_url = reverse_lazy("home")

class CalcularDistancia(SuccessMessageMixin, FormView):
    template_name = "core/calcular_distancia.html"
    form_class = VerificarDistancia
    extra_context = {"title": "Calcular distância"}
    success_url = reverse_lazy("calcular_distancia")
    success_message = "Sucessooo"

    def get_success_message(self, cleaned_data):
        distancia = cleaned_data["distancia"]
        return f"Distância de {distancia:.2f} km, é possível realizar busca."