# Generated by Django 2.1.7 on 2019-02-21 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('modificada', models.BooleanField(default=False)),
                ('descripcion', models.CharField(max_length=256)),
                ('horas_asignadas', models.FloatField()),
                ('horas_disponibles', models.FloatField()),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Cartel')),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Req', 'Requerimiento'), ('Err', 'Error'), ('Tar', 'Tarea'), ('Sub', 'Subtarea'), ('Epi', 'Epic')], max_length=3)),
                ('descripcion', models.CharField(max_length=256)),
                ('codigo', models.CharField(max_length=32, unique=True)),
                ('horas_estimadas', models.FloatField()),
                ('horas_trabajadas', models.FloatField()),
                ('reasignada', models.BooleanField(default=False)),
                ('fecha_produccion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('1', 'Por hacer'), ('2', 'En proceso'), ('3', 'Desarrollado'), ('4', 'En pruebas'), ('5', 'Aprobado por PO'), ('6', 'Hecho'), ('7', 'Pagada'), ('8', 'Por pagar')], max_length=2)),
                ('cartel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Cartel')),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Incidencia')),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_inicio', models.CharField(choices=[('1', 'Por hacer'), ('2', 'En proceso'), ('3', 'Desarrollado'), ('4', 'En pruebas'), ('5', 'Aprobado por PO'), ('6', 'Hecho'), ('7', 'Pagada'), ('8', 'Por pagar')], max_length=2)),
                ('estado_fin', models.CharField(blank=True, choices=[('1', 'Por hacer'), ('2', 'En proceso'), ('3', 'Desarrollado'), ('4', 'En pruebas'), ('5', 'Aprobado por PO'), ('6', 'Hecho'), ('7', 'Pagada'), ('8', 'Por pagar')], max_length=2)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('rol', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_revision', models.DateField()),
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('proyecto', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='planificacion',
            name='asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Responsable'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='incidencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Incidencia'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Sprint'),
        ),
        migrations.AddField(
            model_name='observacion',
            name='planificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Planificacion'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='sprint_fin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sprint_fin', to='tracking.Sprint'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='sprint_inicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sprint_inicio', to='tracking.Sprint'),
        ),
    ]
