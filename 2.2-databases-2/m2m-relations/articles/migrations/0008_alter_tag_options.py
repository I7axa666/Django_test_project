# Generated by Django 4.2 on 2023-04-10 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_scope_options_alter_scope_is_main_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тэги', 'verbose_name_plural': 'Тэги'},
        ),
    ]
