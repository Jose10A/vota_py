# Generated by Django 4.0.1 on 2022-01-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_votos_id_votacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votos',
            name='id_votacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.votaciones'),
        ),
    ]
