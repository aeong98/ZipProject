# Generated by Django 3.2.6 on 2021-08-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210818_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='interest',
            field=models.CharField(choices=[('choice1', 'Choice1'), ('choice2', 'Choice2'), ('choice3', 'Choice3')], default='', max_length=20),
        ),
    ]
