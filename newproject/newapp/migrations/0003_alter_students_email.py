# Generated by Django 4.0.3 on 2022-03-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]