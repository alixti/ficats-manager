# Generated by Django 4.2.7 on 2023-11-23 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paneltrabajador', '0003_remove_cita_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paneltrabajador.mascota'),
        ),
    ]
