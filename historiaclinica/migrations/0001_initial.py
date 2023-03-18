# Generated by Django 3.2.6 on 2023-03-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateTimeField(auto_now_add=True)),
                ('fechaCreacionHistoria', models.DateTimeField(auto_now_add=True)),
                ('estadoCivil', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('antecedentesEnfermedades', models.CharField(max_length=50)),
                ('motivoConsulta', models.CharField(max_length=50)),
            ],
        ),
    ]