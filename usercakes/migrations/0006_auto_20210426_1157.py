# Generated by Django 3.2 on 2021-04-26 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycakes', '0010_alter_cakes_createdat'),
        ('usercakes', '0005_userdetails_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='cart',
            field=models.ManyToManyField(blank=True, to='mycakes.Cakes'),
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='order',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usercakes.order'),
            preserve_default=False,
        ),
    ]
