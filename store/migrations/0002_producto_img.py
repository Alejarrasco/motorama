# Generated by Django 4.0.8 on 2022-12-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(default='null', upload_to='producto/'),
        ),
    ]