# Generated by Django 5.1.6 on 2025-02-25 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='first_name',
        ),
    ]
