# Generated by Django 4.2 on 2023-04-10 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagscop', to='articles.tag', verbose_name='Тэги'),
        ),
    ]
