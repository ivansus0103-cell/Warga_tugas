from django.urls import path
from .views import WargaListView, WargaDetailView,PengaduanListView, WargaCreateView, PengaduanCreateView, WargaUpdateView, WargaDeleteView, PengaduanUpdateView, PengaduanDeleteView


urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('tambah/', WargaCreateView.as_view(), name='warga_tambah'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga_edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga_hapus'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan_tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan_edit'),
    path('pengaduan/<int:pk>/delete/', PengaduanDeleteView.as_view(), name='pengaduan_delete'),
]
