from django.conf.urls import url
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView
from . import views
urlpatterns = [
   url('email/', views.email, name='email'),
   # url('email/', emailView, name='email'),
   # url('success/', successView, name='success'),
   url('blog/', BlogPageView.as_view(), name='blog'),
   url('contact/', ContactPageView.as_view(), name='contact'),
   url('about/', AboutPageView.as_view(), name='about'),
   url('', HomePageView.as_view(), name='index'),
]
