# Generated by Django 4.2 on 2023-04-10 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_scopes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
    ]
