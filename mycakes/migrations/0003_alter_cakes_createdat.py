# Generated by Django 3.2 on 2021-04-24 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycakes', '0002_alter_cakes_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 18, 13, 59, 736041)),
        ),
    ]
