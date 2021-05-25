from django.contrib import admin

# Register your models here.
from .models import registrationmodel,bookroommodel,confirmedpayments

admin.site.register(registrationmodel)
admin.site.register(bookroommodel)
admin.site.register(confirmedpayments)