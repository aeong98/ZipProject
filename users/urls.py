from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('auth/naver/', views.NaverLogin.as_view(), name='naver_login'),
]