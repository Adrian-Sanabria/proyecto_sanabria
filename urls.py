from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from app.views import SucursalViewSet, TramiteViewSet, PagoViewSet, FotoViewSet, DashboardView

router = routers.DefaultRouter()
router.register('sucursales', SucursalViewSet)
router.register('tramites', TramiteViewSet)
router.register('pagos', PagoViewSet)
router.register('fotos', FotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
