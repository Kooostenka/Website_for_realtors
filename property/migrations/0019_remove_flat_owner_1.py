# Generated by Django 2.2.4 on 2019-10-07 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20191007_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_1',
        ),
    ]
