# Generated by Django 3.2.9 on 2021-11-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='fees_in_worls',
            new_name='fees_in_world',
        ),
    ]
