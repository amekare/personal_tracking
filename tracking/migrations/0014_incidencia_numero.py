# Generated by Django 2.2.10 on 2020-04-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0013_auto_20200402_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]