# Generated by Django 3.2.8 on 2022-06-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220630_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]
