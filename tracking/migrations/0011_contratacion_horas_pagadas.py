# Generated by Django 2.2.10 on 2020-03-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0010_contratacion_pago_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacion',
            name='horas_pagadas',
            field=models.FloatField(default=0),
        ),
    ]
