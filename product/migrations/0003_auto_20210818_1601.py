# Generated by Django 3.2.6 on 2021-08-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210818_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shop_Type',
            field=models.CharField(choices=[('오프라인', '오프라인'), ('온라인', '온라인'), ('비매품', '비매품')], default='온라인', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('장식/조명', '장식/조명'), ('DIY/공구', 'DIY/공구'), ('가구', '가구'), ('수납/정리', '수납/정리'), ('패브릭', '패브릭'), ('가전', '가전')], default='가구', max_length=20),
        ),
    ]
