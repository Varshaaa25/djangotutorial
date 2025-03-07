# Generated by Django 5.1.6 on 2025-02-25 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_department_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=12)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
            ],
        ),
    ]
