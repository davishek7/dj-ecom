# Generated by Django 3.2 on 2021-04-20 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='first_name',
            new_name='name',
        ),
    ]