# Generated by Django 2.2 on 2021-07-17 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210716_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='town',
            new_name='province',
        ),
    ]