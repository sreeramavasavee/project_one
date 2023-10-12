from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

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
    
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('School_list')