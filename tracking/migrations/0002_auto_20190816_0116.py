# Generated by Django 2.1.11 on 2019-08-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bitacora_contratacion',
            new_name='BitacoraContratacion',
        ),
        migrations.RenameModel(
            old_name='Bitacora_producto',
            new_name='BitacoraProducto',
        ),
        migrations.RenameModel(
            old_name='Detalle_factura',
            new_name='DetalleFactura',
        ),
        migrations.AlterModelOptions(
            name='contratacion',
            options={'verbose_name': 'Contratación', 'verbose_name_plural': 'Contrataciones'},
        ),
        migrations.AlterModelOptions(
            name='contratista',
            options={'verbose_name': 'Contratista', 'verbose_name_plural': 'Contratistas'},
        ),
        migrations.AlterModelOptions(
            name='detallefactura',
            options={'verbose_name': 'Detalle de factura', 'verbose_name_plural': 'Detalles de factura'},
        ),
        migrations.AlterModelOptions(
            name='factura',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='incidencia',
            options={'verbose_name': 'Incidencia', 'verbose_name_plural': 'Incidencias'},
        ),
        migrations.AlterModelOptions(
            name='observacion',
            options={'ordering': ['fecha'], 'verbose_name': 'Observación', 'verbose_name_plural': 'Observaciones'},
        ),
        migrations.AlterModelOptions(
            name='planificacion',
            options={'ordering': ['sprint', 'fecha_asignada'], 'verbose_name': 'Planificación', 'verbose_name_plural': 'Planificaciones'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterModelOptions(
            name='sprint',
            options={'ordering': ['numero', 'proyecto'], 'verbose_name': 'Sprint', 'verbose_name_plural': 'Sprints'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='horas_utilizadas',
            field=models.FloatField(default=0),
        ),
    ]