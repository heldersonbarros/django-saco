from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    bairro = models.CharField(max_length=20)
    rua = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.bairro}, {self.rua}, {self.numero}"

class Empresa(models.Model):
    cnpj = models.CharField(max_length=20)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cnpj

class Cliente(models.Model):
    pessoa = models.ForeignKey(Pessoa, primary_key=True, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=120)
    celular = models.CharField(max_length=120)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pessoa.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ItemServico(models.Model):
    descricao = models.CharField(max_length=120)

    def __str__(self):
        return self.descricao

class Servico(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
    item_servico = models.ManyToManyField(ItemServico)

    def __str__(self):
        return self.descricao

class Funcionario(models.Model):
    pessoa = models.OneToOneField(Pessoa, primary_key=True, on_delete=models.CASCADE)
    data_admissao = models.DateTimeField(auto_now_add=True, blank=True)
    salario = models.FloatField()
    especialidade = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.pessoa.nome

class OrdemServico(models.Model):
    data_conclusao = models.DateField(blank=True, null=True)
    data_entrada = models.DateField(auto_now=True)
    data_saida = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico)

class RealizacaoServico(models.Model):
    realizado = models.BooleanField(default=False)
    item_servico = models.ManyToManyField(ItemServico)
    item_servico = models.ManyToManyField(OrdemServico)
    funcionario = models.ManyToManyField(Funcionario)