from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer


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

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListAPIView(ListAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = WargaSerializer

class PengaduanDetailAPIView(RetrieveAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = WargaSerializer

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga_list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga_list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm # sesuaikan dengan field di model
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga_list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan_list')

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
