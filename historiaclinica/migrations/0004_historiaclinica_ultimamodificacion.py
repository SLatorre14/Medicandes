# Generated by Django 3.2.6 on 2023-04-14 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinica', '0003_auto_20230317_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='ultimaModificacion',
            field=models.DateTimeField(auto_now_add=True, default='2022-04-13T02:17:44.235Z'),
            preserve_default=False,
        ),
    ]
