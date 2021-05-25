from django.db import models
from django.utils.timezone import now
# Create your models here.
class bookmeetingroommodel(models.Model):
    email=models.CharField(max_length=40,blank=False,default="x")
    room_no=models.CharField(max_length=5,primary_key=True)
    room_type=models.CharField(max_length=50)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    end_date=models.DateField(auto_now=False, auto_now_add=False,default=now)
    class Meta:
        db_table="meetingroombookings"