# Generated by Django 2.2 on 2021-08-17 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20210817_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Product'),
        ),
    ]