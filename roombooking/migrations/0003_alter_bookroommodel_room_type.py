# Generated by Django 3.2.1 on 2021-05-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0002_alter_bookroommodel_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookroommodel',
            name='room_type',
            field=models.CharField(max_length=50),
        ),
    ]
