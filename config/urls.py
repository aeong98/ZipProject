from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# for users app

# for product app
from rest_framework import routers
from product.views import ProductViewSet,ProductCommentViewSet,TagViewSet


router = routers.DefaultRouter()
router.register('product/add',ProductViewSet)
router.register('product/comment', ProductCommentViewSet)
router.register('product/tag',TagViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)