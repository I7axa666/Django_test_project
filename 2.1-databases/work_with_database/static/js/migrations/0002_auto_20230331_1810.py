# Generated by Django 3.1.2 on 2023-03-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id_phone',
            field=models.IntegerField(),
        ),
    ]
