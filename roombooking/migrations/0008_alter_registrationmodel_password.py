# Generated by Django 3.2.1 on 2021-08-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0007_alter_registrationmodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
