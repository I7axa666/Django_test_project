# Generated by Django 4.2 on 2023-04-10 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagscop', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
