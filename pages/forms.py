from django import forms
from .models import Mails

from .models import Mails


class EmailForm(forms.ModelForm):
   email = forms.EmailField(max_length=200,
                            widget=forms.TextInput(attrs={'class': "form-control", 'id': "clientemail"}))
   message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
   subject = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

   class Meta:
      model = Mails
      fields = ('email', 'subject', 'message', 'document',)


# from django import forms
#
#
# class ContactForm(forms.Form):
#    message = forms.CharField(widget=forms.Textarea, required=True)
#    name = forms.CharField(required=True)
#    from_email = forms.CharField(required=True)
#    subject = forms.CharField(widget=forms.Textarea, required=True)
#
