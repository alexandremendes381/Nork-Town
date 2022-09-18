from django import forms
from .models import Cliente, Locacao

class ClienteForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices = Cliente.STATUS, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome','cpf','status')


class LocacaoForm(forms.ModelForm):


    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(status='ATIVO'),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    
    tipo = forms.ChoiceField(choices=Locacao.TIPO,
                             widget=forms.Select(attrs={'class': 'form-control'}))
    
    cor = forms.ChoiceField(choices=Locacao.COR,
                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Locacao
        fields = ('cliente','tipo','cor')
