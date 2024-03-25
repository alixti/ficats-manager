# Generated by Django 4.2.7 on 2023-11-22 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=65)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=30)),
                ('stock_disponible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('numero_chip', models.IntegerField()),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('historial_medico', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paneltrabajador.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.IntegerField(primary_key=True, serialize=False)),
                ('total_pagar', models.IntegerField()),
                ('detalle', models.TextField()),
                ('estado_pago', models.CharField(max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paneltrabajador.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('n_cita', models.IntegerField(primary_key=True, serialize=False)),
                ('numero_chip', models.BigIntegerField()),
                ('estado', models.CharField(max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paneltrabajador.cliente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
