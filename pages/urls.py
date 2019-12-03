from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView, emailView, successView

urlpatterns = [
   path('email/', emailView, name='email'),
   path('success/', successView, name='success'),
   path('blog/', BlogPageView.as_view(), name='blog'),
   path('contact/', ContactPageView.as_view(), name='contact'),
   path('about/', AboutPageView.as_view(), name='about'),
   path('', HomePageView.as_view(), name='index'),
]
