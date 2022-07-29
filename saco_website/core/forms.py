from django import forms
from . models import Cliente, Endereco, Funcionario, OrdemServico, Pessoa, Veiculo
from geopy import distance

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('tipo', 'celular')

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('placa', 'marca', 'modelo')

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('__all__')

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('salario', 'especialidade', 'foto')

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = '__all__'
        widgets = {
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
            'data_conclusao': forms.DateInput(attrs={'type': 'date'})
        }

class VerificarDistancia(forms.Form):
    latitude = forms.FloatField(min_value=-90, max_value=90)
    longitude = forms.FloatField(min_value=-180, max_value=180)

    def clean(self):
        cleaned_data = super().clean()

        longitude = cleaned_data["longitude"]
        latitude = cleaned_data["latitude"]
        
        distancia = distance.geodesic((-7.956002, -38.296028), (latitude, longitude)).kilometers

        if distancia > 15:
            raise forms.ValidationError(f"Distância de {distancia:.2f} km, não é possível realizar a busca.")

        cleaned_data["distancia"] = distancia

        return cleaned_data