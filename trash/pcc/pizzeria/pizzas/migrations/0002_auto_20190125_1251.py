# Generated by Django 2.1.5 on 2019-01-25 12:51

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizzas',
            new_name='Pizza',
        ),
    ]