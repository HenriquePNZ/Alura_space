from django import forms
from apps.galeria.models import Fotografia

# Montado dessa maneira porque ESTÁ vinculado a um modelo de banco de dados (Fotografia)
# Herda automaticamente os campos do modelo e garante que o formulário sempre reflita a estrutura do BD

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'descricao' : 'Descrição',
            'data_fotografia' : 'Data de registro',
            'usuario' : 'Usuário'
        }
        
        widgets = {
            'nome': forms.TextInput(attrs = {'class' : 'form-control'}),
            'legenda': forms.TextInput(attrs = {'class' : 'form-control'}),
            'categoria': forms.Select(attrs = {'class' : 'form-control'}),
            'descricao': forms.Textarea(attrs = {'class' : 'form-control'}),
            'foto': forms.FileInput(attrs = {'class' : 'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%y',
                attrs = {
                    'type' : 'date',
                    'class' : 'form-control'
                    }
                ),
            'usuario': forms.Select(attrs = {'class' : 'form-control'}),
        }