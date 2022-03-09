# Generated by Django 3.2.8 on 2022-01-12 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '__first__'),
        ('businesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('is_on_fair', models.BooleanField(default=True, verbose_name='is on fair')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
                ('publicity_duration', models.DurationField(verbose_name='publicity duration')),
            ],
            options={
                'verbose_name': 'package',
                'verbose_name_plural': 'packages',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.FloatField(verbose_name='quantity')),
                ('customer', models.ForeignKey(limit_choices_to={'groups__name': 'customer', 'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='offers.package', verbose_name='packages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='package',
            name='customers',
            field=models.ManyToManyField(through='offers.Purchase', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='package',
            name='products',
            field=models.ManyToManyField(related_name='packages', to='products.Product'),
        ),
        migrations.AddField(
            model_name='package',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='businesses.shop'),
        ),
    ]
