# Generated by Django 3.0.3 on 2020-02-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20200222_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='col_id',
        ),
    ]
