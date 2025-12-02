from django.urls import path, include
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView , PengaduanDetailAPIView, WargaViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', WargaViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
    path('warga/', WargaListAPIView.as_view(), name='api_warga_list'),
    path('warga/<int:pk>', WargaDetailAPIView.as_view(), name='api_warga_Detail'),
    path('Pengaduan/', PengaduanListAPIView.as_view(), name='api_Pengaduan_list'),
    path('Pengaduan/<int:pk>', PengaduanDetailAPIView.as_view(), name='api_Pengaduan_detail'),
]
