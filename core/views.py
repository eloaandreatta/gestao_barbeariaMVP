from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Profissional, Atendimento
from .forms import AtendimentoForm
@login_required
def painel(request):
    ats=Atendimento.objects.all()
    return render(request,'core/painel.html',{'total':ats.count(),'valor':ats.aggregate(Sum('valor'))['valor__sum'] or 0,'clientes':Cliente.objects.count(),'profissionais':Profissional.objects.filter(ativo=True).count()})
@login_required
def novo_atendimento(request):
    form=AtendimentoForm(request.POST or None)
    form.fields['profissional'].queryset=Profissional.objects.filter(ativo=True)
    if request.method=='POST' and form.is_valid():
        a=form.save(); messages.success(request,'Atendimento registrado com sucesso!'); return redirect('historico',cliente_id=a.cliente_id)
    return render(request,'core/novo_atendimento.html',{'form':form})
@login_required
def historico(request,cliente_id):
    cliente=get_object_or_404(Cliente,pk=cliente_id)
    ats=cliente.atendimentos.select_related('servico','profissional')
    return render(request,'core/historico.html',{'cliente':cliente,'atendimentos':ats,'valor_total':ats.aggregate(Sum('valor'))['valor__sum'] or 0})
