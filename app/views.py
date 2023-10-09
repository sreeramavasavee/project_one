from django.shortcuts import render
from django.views.generic import ListView
from app.models import *

# Create your views here.
class Schoollist(ListView):
    model=School
    context_object_name='schools'