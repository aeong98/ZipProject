from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=20) #상품명
    # pub_date = models.DateTimeField(default=timezone.now) #생성날짜/시간
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="post_products",default='') #작성자
    content = models.TextField(default='') #설명
    image = models.ImageField(upload_to='images/',blank=True) #상품이미지
    price = models.IntegerField(default=0) #가격

    SHOP_CHOICES = {
        ('온라인','온라인'),
        ('오프라인','오프라인'),
        ('비매품', '비매품'),
    }
    shop_Type = models.CharField(max_length=20,choices=SHOP_CHOICES,default='온라인')
    shop_URL_Location = models.CharField(max_length=500, default='') #구매링크/위치

    TYPE_CHOICES = {
        ('가구','가구'),
        ('패브릭','패브릭'),
        ('장식/조명','장식/조명'),
        ('DIY/공구','DIY/공구'),
        ('가전','가전'),
        ('수납/정리','수납/정리')
    }
    type = models.CharField(max_length=20,choices=TYPE_CHOICES,default='가구') #상품 카테고리
    tags = models.ManyToManyField('ProductTag',blank=True)

    def __str__(self):
        return str(self.title)


class ProductComment(models.Model) :
    product = models.ForeignKey('Product',related_name='product_comments',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.product)

class ProductTag(models.Model):
    name = models.CharField(max_length=10, unique=True,blank=True)

    def __str__(self):
        return str(self.name)