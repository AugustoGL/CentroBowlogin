# Generated by Django 4.2.7 on 2023-12-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CentroDeBowling', '0004_reserva_estado_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado_reserva',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.estadoreserva'),
        ),
    ]
