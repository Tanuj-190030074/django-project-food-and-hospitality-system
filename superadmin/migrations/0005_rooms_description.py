# Generated by Django 3.2.1 on 2021-05-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0004_auto_20210510_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='description',
            field=models.TextField(default='add some description about room'),
        ),
    ]