# Generated by Django 3.2.4 on 2021-07-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PRODUCTOS', '0002_carrito'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carrito',
        ),
    ]