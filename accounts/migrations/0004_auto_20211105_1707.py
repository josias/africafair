# Generated by Django 3.2.8 on 2021-11-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'visitor'), (2, 'customer'), (3, 'seller'), (4, 'owner'), (5, 'editor')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(to='accounts.Role'),
        ),
    ]
