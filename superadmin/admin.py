from django.contrib import admin
from . models import DineInTables,Rooms,superadminlogin,meetingrooms

admin.site.register(DineInTables)
admin.site.register(Rooms)
admin.site.register(superadminlogin)
admin.site.register(meetingrooms)
# Register your models here.
