# Generated by Django 4.2.6 on 2023-11-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_apellido_aficionado_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='edad',
            field=models.IntegerField(default=18),
        ),
    ]