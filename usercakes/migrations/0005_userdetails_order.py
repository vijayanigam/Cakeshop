# Generated by Django 3.2 on 2021-04-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercakes', '0004_alter_order_cakes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='order',
            field=models.ManyToManyField(blank=True, null=True, to='usercakes.Order'),
        ),
    ]