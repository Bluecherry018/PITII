# Generated by Django 5.1 on 2024-11-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0016_rename_compromissos_planner_compromissos1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='compromissos',
            field=models.TextField(blank=True),
        ),
    ]
