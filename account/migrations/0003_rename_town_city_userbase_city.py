# Generated by Django 3.2 on 2021-04-20 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_first_name_userbase_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='town_city',
            new_name='city',
        ),
    ]
