# Generated by Django 3.2.5 on 2021-07-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20210703_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('패브릭', '패브릭'), ('수납/정리', '수납/정리'), ('DIY/공구', 'DIY/공구'), ('가구', '가구'), ('홈데코/조명', '홈데코/조명'), ('가전', '가전')], max_length=20),
        ),
        migrations.AlterField(
            model_name='itemcomment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
