# Generated by Django 5.1 on 2024-08-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_delete_sonoregistro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='horas',
            field=models.PositiveIntegerField(default='', verbose_name='Quantas horas de Sono'),
        ),
    ]