# Generated by Django 2.0.2 on 2018-02-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='name',
            new_name='owner_name',
        ),
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
