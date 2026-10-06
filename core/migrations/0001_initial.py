from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
      migrations.CreateModel(name='Cliente',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nome',models.CharField(max_length=120)),('telefone',models.CharField(blank=True,max_length=20)),('criado_em',models.DateTimeField(auto_now_add=True))]),
      migrations.CreateModel(name='Profissional',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nome',models.CharField(max_length=120)),('ativo',models.BooleanField(default=True))]),
      migrations.CreateModel(name='Servico',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('nome',models.CharField(max_length=120,unique=True)),('valor_padrao',models.DecimalField(decimal_places=2,max_digits=8)),('ativo',models.BooleanField(default=True))]),
      migrations.CreateModel(name='Atendimento',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('data_hora',models.DateTimeField()),('valor',models.DecimalField(decimal_places=2,max_digits=8)),('observacao',models.CharField(blank=True,max_length=300)),('criado_em',models.DateTimeField(auto_now_add=True)),('cliente',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='atendimentos',to='core.cliente')),('profissional',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='atendimentos',to='core.profissional')),('servico',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='atendimentos',to='core.servico'))],options={'ordering':['-data_hora']})]
