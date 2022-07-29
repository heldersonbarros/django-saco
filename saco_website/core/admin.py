from django.contrib import admin

# Register your models here.
from . models import Pessoa, Funcionario, Cliente, Endereco, Empresa

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Empresa)