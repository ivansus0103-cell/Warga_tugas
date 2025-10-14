from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan

class WargaListView(ListView):
    model = Warga
    template_name = 'warga_list.html'
    context_object_name = 'object_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_List.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor'] 
