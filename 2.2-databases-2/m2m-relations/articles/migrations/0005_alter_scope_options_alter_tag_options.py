# Generated by Django 4.2 on 2023-04-10 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэги', 'verbose_name_plural': 'Тэги'},
        ),
    ]
