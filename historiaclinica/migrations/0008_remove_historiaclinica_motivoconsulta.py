# Generated by Django 3.2.6 on 2023-05-05 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinica', '0007_remove_historiaclinica_ultimamodificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='motivoConsulta',
        ),
    ]
