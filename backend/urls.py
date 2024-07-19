from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import OnePieceCardViewSet, FusionWorldCardViewSet

# Define API routes using DefaultRouter
router = DefaultRouter()
router.register(r'one-piece', OnePieceCardViewSet)
router.register(r'fusion-world-cards', FusionWorldCardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
