from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView
from .forms import ContactForm


# Create your views here.
class HomePageView(TemplateView):
   template_name = 'index.html'


class AboutPageView(TemplateView):
   template_name = 'about.html'


class ContactPageView(TemplateView):
   template_name = 'contact.html'


class BlogPageView(TemplateView):
   template_name = 'blog.html'


def emailView(request):
   if request.method == 'GET':
      form = ContactForm()
   else:
      form = ContactForm(request.POST)
      if form.is_valid():
         message = form.cleaned_data['message']
         # name = form.cleaned_data['name']
         from_email = form.cleaned_data['from_email']
         subject = form.cleaned_data['subject']
         try:
            send_mail(subject, message, from_email, ['maqsoodshah@ncloud.hk'])
         except BadHeaderError:
            return HttpResponse('Invalid header found.')
         return redirect('success')
   return render(request, "email.html", {'form': form})


def successView(request):
   return HttpResponse('Success! Thank you for message.')
