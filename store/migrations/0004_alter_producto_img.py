# Generated by Django 4.0.8 on 2022-12-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]