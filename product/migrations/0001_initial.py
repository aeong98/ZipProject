# Generated by Django 3.2.6 on 2021-08-18 06:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(default='')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.IntegerField(default=0)),
                ('shop_Type', models.CharField(choices=[('비매품', '비매품'), ('오프라인', '오프라인'), ('온라인', '온라인')], default='온라인', max_length=20)),
                ('shop_URL_Location', models.CharField(default='', max_length=500)),
                ('type', models.CharField(choices=[('수납/정리', '수납/정리'), ('가구', '가구'), ('가전', '가전'), ('장식/조명', '장식/조명'), ('DIY/공구', 'DIY/공구'), ('패브릭', '패브릭')], default='가구', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.Tag'),
        ),
    ]
