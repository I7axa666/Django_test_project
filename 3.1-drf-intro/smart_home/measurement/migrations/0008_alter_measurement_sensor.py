# Generated by Django 4.2 on 2023-04-29 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_rename_dt_measurement_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]
