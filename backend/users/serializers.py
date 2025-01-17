# for Custom Resister
from .models import CustomUser
from django.db import transaction
from rest_framework import fields, serializers
from rest_auth.registration.serializers import RegisterSerializer

# for Profile
class CustomRegisterSerializer(RegisterSerializer):
		# 추가할 속성
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    @transaction.atomic # 부분적으로 실행되다가 중단되지 않는 것을 보장
    def save(self, request):
        # user = super(CustomRegisterSerializer, self).save(request)
        user = super().save(request)
				# 데이터 입력
        user.first_name= self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomUser
      fields = ['username', 'email', 'first_name', 'last_name', 'description', 'profile_image', 'header_image','interest',]