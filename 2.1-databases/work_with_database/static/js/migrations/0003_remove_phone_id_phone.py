# Generated by Django 3.1.2 on 2023-03-31 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20230331_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='id_phone',
        ),
    ]
