# Generated by Django 2.2 on 2019-12-19 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]