from rest_framework import serializers
from .models import Product,Product_comment,Tag

class ProductCommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product_comment
        fields ='__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer) :
    image = serializers.ImageField(use_url=True)
    comments = ProductCommentSerializer(many=True, read_only=True)
    class Meta :
        model = Product
        fields = ('title','pub_date','user','content','image','price'
        ,'shop_Type','shop_URL_Location','type','tags','comments')

