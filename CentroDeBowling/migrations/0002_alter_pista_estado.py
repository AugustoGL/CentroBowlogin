# Generated by Django 4.2.7 on 2023-12-07 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CentroDeBowling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pista',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CentroDeBowling.estadopista'),
        ),
    ]