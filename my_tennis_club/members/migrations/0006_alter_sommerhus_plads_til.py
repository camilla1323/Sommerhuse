# Generated by Django 5.0.2 on 2024-05-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_sommerhus_sommerhus_id_sommerhus_ejer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sommerhus',
            name='Plads_til',
            field=models.IntegerField(null=True),
        ),
    ]
