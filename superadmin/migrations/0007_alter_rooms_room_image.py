# Generated by Django 3.2.1 on 2021-05-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0006_alter_rooms_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
