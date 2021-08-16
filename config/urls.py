from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# for users app
from users.views import index
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
    path('', index, name="index"),
    path('users/', include('users.urls')),
]