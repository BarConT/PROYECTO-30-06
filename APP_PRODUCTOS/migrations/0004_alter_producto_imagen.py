# Generated by Django 3.2.4 on 2021-07-02 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PRODUCTOS', '0003_delete_carrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null='True', upload_to='productos'),
        ),
    ]
