from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Warga

class WargaListView(ListView):
    model = Warga
    template_name = 'warga_list.html'
    context_object_name = 'object_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'