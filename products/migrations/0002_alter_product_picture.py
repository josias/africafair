# Generated by Django 3.2.8 on 2022-01-31 19:03

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=versatileimagefield.fields.VersatileImageField(default='static/assets/img/products_pictures/af-showcase-1.png', upload_to='static/assets/img/products_pictures/', verbose_name='product'),
        ),
    ]
