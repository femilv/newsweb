# Generated by Django 5.0.3 on 2024-04-14 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0002_news_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]