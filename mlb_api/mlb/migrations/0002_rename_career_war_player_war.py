# Generated by Django 4.0.2 on 2022-02-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='career_war',
            new_name='war',
        ),
    ]
