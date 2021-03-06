# Generated by Django 3.2.8 on 2022-01-12 15:31

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='fair_sites.country')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'quarter',
                'verbose_name_plural': 'quarters',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towns', to='fair_sites.department')),
            ],
            options={
                'verbose_name': 'town',
                'verbose_name_plural': 'towns',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zones', to='fair_sites.town')),
            ],
            options={
                'verbose_name': 'zone',
                'verbose_name_plural': 'zones',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street', models.CharField(default='anywhere', max_length=50, verbose_name='street')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='address')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='fair_sites.quarter')),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': 'sites',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='quarter',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quaters', to='fair_sites.zone'),
        ),
    ]
