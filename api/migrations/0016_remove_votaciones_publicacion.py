# Generated by Django 4.0.1 on 2022-03-22 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_datos_empleados_alter_candidatos_id_votaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votaciones',
            name='publicacion',
        ),
    ]
