# Generated by Django 5.1 on 2024-08-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='null', upload_to='photo/profile/%Y/%m/%d/'),
        ),
    ]
