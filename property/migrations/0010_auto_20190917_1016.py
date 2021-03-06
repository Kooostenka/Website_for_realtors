# Generated by Django 2.2.4 on 2019-09-17 07:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20190916_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_1',
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('phone_pure', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
