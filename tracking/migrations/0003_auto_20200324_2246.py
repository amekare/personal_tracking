# Generated by Django 2.2.10 on 2020-03-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20190816_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bitacoraproducto',
            options={'ordering': ('producto', 'fecha'), 'verbose_name': 'Bitácora de producto', 'verbose_name_plural': 'Bitácoras de productos'},
        ),
        migrations.AlterModelOptions(
            name='contratacion',
            options={'ordering': ('proyecto__codigo', 'tipo'), 'verbose_name': 'Contratación', 'verbose_name_plural': 'Contrataciones'},
        ),
        migrations.AlterModelOptions(
            name='contratista',
            options={'ordering': ('apellido1', 'apellido2'), 'verbose_name': 'Contratista', 'verbose_name_plural': 'Contratistas'},
        ),
        migrations.AlterModelOptions(
            name='detallefactura',
            options={'ordering': ('factura',), 'verbose_name': 'Detalle de factura', 'verbose_name_plural': 'Detalles de factura'},
        ),
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ('contratacion', 'fecha'), 'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='incidencia',
            options={'ordering': ('producto__contratacion', 'codigo'), 'verbose_name': 'Incidencia', 'verbose_name_plural': 'Incidencias'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ('contratacion', 'numero'), 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ('codigo',), 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='horas_pagadas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='presupuesto_adjudicado',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='presupuesto_consumido',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]