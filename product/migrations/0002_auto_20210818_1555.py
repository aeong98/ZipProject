# Generated by Django 3.2.6 on 2021-08-18 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_Type',
            field=models.CharField(choices=[('오프라인', '오프라인'), ('비매품', '비매품'), ('온라인', '온라인')], default='온라인', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('가구', '가구'), ('DIY/공구', 'DIY/공구'), ('가전', '가전'), ('수납/정리', '수납/정리'), ('패브릭', '패브릭'), ('장식/조명', '장식/조명')], default='가구', max_length=20),
        ),
    ]