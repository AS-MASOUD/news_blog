# Generated by Django 5.1 on 2024-09-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_about_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(default='null', max_length=1000),
        ),
    ]
