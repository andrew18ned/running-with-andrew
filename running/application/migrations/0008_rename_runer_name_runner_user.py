# Generated by Django 4.0.5 on 2022-06-11 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_remove_runner_name_runner_runer_name_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runner',
            old_name='runer_name',
            new_name='user',
        ),
    ]
