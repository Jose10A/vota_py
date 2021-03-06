# Generated by Django 4.0.1 on 2022-01-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_empleados_email_remove_empleados_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='user',
        ),
        migrations.AddField(
            model_name='empleados',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empleados',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleados',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleados',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
