from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from django.views.generic import TemplateView
# from .forms import ContactForm
from django.core.files.storage import FileSystemStorage
from .forms import EmailForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.
class HomePageView(TemplateView):
   template_name = 'index.html'


class AboutPageView(TemplateView):
   template_name = 'about.html'


class ContactPageView(TemplateView):
   template_name = 'contact.html'


class BlogPageView(TemplateView):
   template_name = 'blog.html'


def email(request):
   if request.method == "POST":
      form = EmailForm(request.POST, request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.published_date = timezone.now()
         post.save()
         email = request.POST.get('email')
         subject = request.POST.get('subject')
         message = request.POST.get('message')
         document = request.FILES.get('document')
         email_from = settings.EMAIL_HOST_USER
         recipient_list = [email]
         email = EmailMessage(subject, message, email_from, recipient_list)
         base_dir = 'media/documents/'
         email.attach_file('media/documents/' + str(document))
         email.send()
      else:
         form = EmailForm()
         return HttpResponseRedirect(request, 'pages/contact.html', {'form': form})
