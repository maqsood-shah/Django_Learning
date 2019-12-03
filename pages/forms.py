from django import forms


class ContactForm(forms.Form):
   message = forms.CharField(widget=forms.Textarea, required=True)
   name = forms.CharField(required=True)
   from_email = forms.CharField(required=True)
   subject = forms.CharField(widget=forms.Textarea, required=True)

