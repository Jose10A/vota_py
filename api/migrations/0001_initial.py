# Generated by Django 4.0.1 on 2022-01-11 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField()),
                ('apellidos', models.TextField()),
                ('no_expediente', models.TextField()),
                ('verificado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='puestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='votaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('publicacion', models.DateTimeField()),
                ('cierre', models.DateTimeField()),
                ('convocatoria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='votos_historicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('id_candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.candidatos')),
                ('id_votacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.votaciones')),
            ],
        ),
        migrations.CreateModel(
            name='votos_empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_votacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.votaciones')),
                ('id_votante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='votos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.candidatos')),
                ('id_votaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.votaciones')),
            ],
        ),
        migrations.AddField(
            model_name='candidatos',
            name='id_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empleados'),
        ),
        migrations.AddField(
            model_name='candidatos',
            name='id_puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.puestos'),
        ),
    ]