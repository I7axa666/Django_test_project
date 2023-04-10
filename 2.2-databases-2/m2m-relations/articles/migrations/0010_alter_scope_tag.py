# Generated by Django 4.2 on 2023-04-10 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_scope_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
