# Generated by Django 4.2.6 on 2023-11-06 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_articles_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='img',
        ),
    ]
