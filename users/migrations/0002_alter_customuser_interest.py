# Generated by Django 3.2.6 on 2021-08-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='interest',
            field=models.CharField(choices=[('choice2', 'Choice2'), ('choice1', 'Choice1'), ('choice3', 'Choice3')], default='', max_length=20),
        ),
    ]