from django import forms
from .models import Atendimento
class AtendimentoForm(forms.ModelForm):
    class Meta:
        model=Atendimento
        fields=['cliente','profissional','servico','data_hora','valor','observacao']
        widgets={'data_hora':forms.DateTimeInput(attrs={'type':'datetime-local'}),'observacao':forms.Textarea(attrs={'rows':3})}
    def clean_valor(self):
        v=self.cleaned_data['valor']
        if v < 0: raise forms.ValidationError('Informe um valor válido para o atendimento.')
        return v
