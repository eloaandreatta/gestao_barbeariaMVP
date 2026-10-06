from django.contrib import admin
from .models import Cliente,Profissional,Servico,Atendimento
admin.site.register([Cliente,Profissional,Servico,Atendimento])
