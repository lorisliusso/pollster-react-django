from django.urls import path
from django.views.generic import TemplateView
from . import views

from . import views


urlpatterns= [
    path('', TemplateView.as_view(template_name='index.html')),
    path('hello/', views.sayHello, name='hello Loris'),
    path('questions/', views.getQuestions, name='questions'),
    path('choices/', views.getChoices, name='choices'),
    
]