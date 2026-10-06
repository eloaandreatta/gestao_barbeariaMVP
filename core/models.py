from django.db import models
class Cliente(models.Model):
    nome=models.CharField(max_length=120)
    telefone=models.CharField(max_length=20,blank=True)
    criado_em=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.nome
class Profissional(models.Model):
    nome=models.CharField(max_length=120)
    ativo=models.BooleanField(default=True)
    def __str__(self): return self.nome
class Servico(models.Model):
    nome=models.CharField(max_length=120,unique=True)
    valor_padrao=models.DecimalField(max_digits=8,decimal_places=2)
    ativo=models.BooleanField(default=True)
    def __str__(self): return self.nome
class Atendimento(models.Model):
    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT,related_name='atendimentos')
    profissional=models.ForeignKey(Profissional,on_delete=models.PROTECT,related_name='atendimentos')
    servico=models.ForeignKey(Servico,on_delete=models.PROTECT,related_name='atendimentos')
    data_hora=models.DateTimeField()
    valor=models.DecimalField(max_digits=8,decimal_places=2)
    observacao=models.CharField(max_length=300,blank=True)
    criado_em=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['-data_hora']
