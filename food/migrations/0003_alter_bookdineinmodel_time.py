# Generated by Django 3.2.1 on 2021-05-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_bookdineinmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdineinmodel',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
