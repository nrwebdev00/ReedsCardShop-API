# Generated by Django 4.1 on 2022-08-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_collector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]