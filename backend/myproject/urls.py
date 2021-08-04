from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('curation/',views.curation,name="curation"),
    path('sh_page/',views.sh_page,name="sh_page"),
    path('zip_page/',views.zip_page,name="zip_page"),

    path('admin/', admin.site.urls),
    path('item/',include('item.urls')),
    path('accounts/',include('accounts.urls')),
    path('new/',include('new.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)