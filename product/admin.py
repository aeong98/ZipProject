from django.contrib import admin
from .models import Product,Product_comment,Tag

admin.site.register(Product)
admin.site.register(Product_comment)
admin.site.register(Tag)