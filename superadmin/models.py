from django.db import models
from datetime import date
# Create your models here.
class DineInTables(models.Model):
    table_no=models.CharField(max_length=10,primary_key=True)
    is_available=models.BooleanField(default=True)
    capacity=models.IntegerField(default=1)

class Rooms(models.Model):
    room_no=models.CharField(max_length=5,primary_key=True)
    room_choices=(('king guestroom','king guestroom'),('king deluxe guestroom','king deluxe guestroom'),('twin guestroom','twin guestroom'))
    room_type=models.CharField(max_length=50,choices=room_choices)
    is_available=models.BooleanField(default=True)
    description=models.TextField(default="add some description about room")
    price=models.FloatField(default=1.00)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media")
    bookcount=models.IntegerField(default=0)
    class Meta:
        db_table="rooms"

class superadminlogin(models.Model):
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="admindata"

class meetingrooms(models.Model):
    room_no=models.CharField(max_length=5,primary_key=True)
    room_choices=(('conference room','conference room'),('ball room','ball room'))
    room_type=models.CharField(max_length=50,blank=False,choices=room_choices)
    is_available=models.BooleanField(default=True)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    class Meta:
        db_table="meetingrooms"