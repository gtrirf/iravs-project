from .models import Feedbacks
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['fullname', 'email_or_number', 'body']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update({'class': 'form-control', 'id': 'id_fullname'})
        self.fields['email_or_number'].widget.attrs.update({'class': 'form-control', 'id': 'id_email_or_number'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'id': 'id_body', 'rows': 5})
