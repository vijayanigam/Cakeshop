# Generated by Django 3.2 on 2021-04-26 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usercakes', '0007_alter_userdetails_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usercakes.order'),
        ),
    ]
