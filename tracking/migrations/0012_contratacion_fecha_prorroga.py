# Generated by Django 2.2.10 on 2020-03-31 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0011_contratacion_horas_pagadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacion',
            name='fecha_prorroga',
            field=models.DateField(blank=True, null=True),
        ),
    ]
