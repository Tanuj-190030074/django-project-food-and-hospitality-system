# Generated by Django 3.2.1 on 2021-05-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0009_alter_rooms_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='bookcount',
            field=models.IntegerField(default=0),
        ),
    ]