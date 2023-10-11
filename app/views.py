from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from app.models import *

# Create your views here.
class home(TemplateView):
    template_name='app/home.html'

class School_list(ListView):
    model=School
    context_object_name='schools'

class School_details(DetailView):
    model=School
    context_object_name='schoolobj'

class School_create(CreateView):
    model=School
    fields='__all__'
    