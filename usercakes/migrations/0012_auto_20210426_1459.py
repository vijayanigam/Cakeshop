# Generated by Django 3.2 on 2021-04-26 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercakes', '0011_auto_20210426_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pending',
        ),
    ]
