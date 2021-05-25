# Generated by Django 3.2.1 on 2021-05-17 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookmeetingroommodel',
            fields=[
                ('email', models.CharField(default='x', max_length=40)),
                ('room_no', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'meetingroombookings',
            },
        ),
    ]