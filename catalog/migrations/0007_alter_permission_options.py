# Generated by Django 3.2.13 on 2023-06-27 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20230627_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('read_authors_and_books', 'Accès au listing des auteurs et des livres.'),)},
        ),
    ]
