# Generated by Django 4.2.6 on 2023-11-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aficionado',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='aventurero',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='Apellido',
            new_name='apellido',
        ),
    ]
