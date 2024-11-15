# Generated by Django 5.1 on 2024-08-27 17:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_horas_entry_informe_entry_sono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='horas',
            field=models.CharField(default='', max_length=2, verbose_name='Quantas horas de Sono'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(choices=[('😀', '😀 Feliz'), ('😐', '😐 Indiferente'), ('😞', '😞 Triste')], default='😴 Bom', max_length=1, verbose_name='Humor'),
        ),
        migrations.CreateModel(
            name='SonoRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualidade', models.CharField(choices=[('😴 Bom', '😴 Bom'), ('🥱\tInsônia', '🥱 Insônia'), ('😫 Ruim', '😫 Ruim')], default='😴 Bom', max_length=100, verbose_name='Qualidade do Sono')),
                ('horas', models.PositiveIntegerField(verbose_name='Quantas horas de Sono')),
                ('informe', models.TextField(default='', verbose_name='Descreva o seu sono')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sono_registros', to='entries.entry')),
            ],
        ),
    ]
