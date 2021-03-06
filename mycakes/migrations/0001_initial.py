# Generated by Django 3.2 on 2021-04-23 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('cakeid', models.AutoField(primary_key=True, serialize=False)),
                ('createdat', models.DateTimeField(default=datetime.datetime(2021, 4, 23, 13, 33, 16, 235264))),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=550)),
                ('type', models.CharField(max_length=550)),
                ('ingredients', models.CharField(max_length=250)),
                ('eggless', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cakeimages/')),
                ('flavour', models.CharField(max_length=550)),
                ('price', models.FloatField()),
                ('weight', models.IntegerField()),
                ('rating', models.FloatField(default=4.5)),
                ('review', models.IntegerField(default=4)),
                ('likes', models.IntegerField(default=4)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
