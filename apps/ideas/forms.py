from django import forms
from .models import Ideas, ReplyToIdea

class IdeasForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReplyToIdeaForm(forms.ModelForm):
    class Meta:
        model = ReplyToIdea
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
