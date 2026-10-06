import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from core.models import Cliente,Profissional,Servico,Atendimento
@pytest.mark.django_db
def test_painel_exige_login(client):
    r=client.get(reverse('painel')); assert r.status_code==302 and '/login/' in r.url
@pytest.mark.django_db
def test_registra_atendimento_e_redireciona(client):
    u=User.objects.create_user('admin',password='SenhaForte123!'); client.login(username='admin',password='SenhaForte123!')
    c=Cliente.objects.create(nome='Lucas Almeida'); p=Profissional.objects.create(nome='Carlos Silva'); s=Servico.objects.create(nome='Corte Masculino',valor_padrao=40)
    r=client.post(reverse('novo_atendimento'),{'cliente':c.id,'profissional':p.id,'servico':s.id,'data_hora':timezone.now().strftime('%Y-%m-%dT%H:%M'),'valor':'40.00','observacao':'Corte tradicional'})
    assert r.status_code==302; assert Atendimento.objects.count()==1
@pytest.mark.django_db
def test_valor_negativo_rejeitado(client):
    u=User.objects.create_user('admin',password='SenhaForte123!'); client.login(username='admin',password='SenhaForte123!')
    c=Cliente.objects.create(nome='Teste'); p=Profissional.objects.create(nome='Profissional'); s=Servico.objects.create(nome='Barba',valor_padrao=30)
    r=client.post(reverse('novo_atendimento'),{'cliente':c.id,'profissional':p.id,'servico':s.id,'data_hora':timezone.now().strftime('%Y-%m-%dT%H:%M'),'valor':'-1'})
    assert r.status_code==200; assert Atendimento.objects.count()==0
