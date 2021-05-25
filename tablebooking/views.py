from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from . models import bookmeetingroommodel
from superadmin.models import meetingrooms
import datetime

def ballroom(request):
    if request.session.get("email",None):
        return render(request,"ballroom.html")
    else:
        return redirect("loginpage")

def bigroom(request):
    if request.session.get("email",None):
        return render(request,"bigroom.html")
    else:
        return redirect("loginpage")

def conf(request):
    if request.session.get("email",None):
        return render(request,"conf.html")
    else:
        return redirect("loginpage")

def ballsuccess(request):
    if request.session.get("email",None):
        return render(request,"ballsuccess.html")
    else:
        return redirect("loginpage")

def consuccess(request):
    if request.session.get("email",None):
        return render(request,"consuccess.html")
    else:
        return redirect("loginpage")

def bookballroom(request):
    if request.session.get("email",None):
        if request.method=="POST":
            try:
                start_date=request.POST["ballstartdate"]
                end_date=request.POST["ballenddate"]
                email=request.session["email"]
                room_type="ball room"
                x=meetingrooms.objects.filter(Q(is_available=True)&Q(room_type=room_type))[0]
                room_no=x.room_no
                x.is_available=False
                x.save()
                z=bookmeetingroommodel(email=email,room_no=room_no,room_type=room_type,start_date=start_date,end_date=end_date)
                z.save()
                return render(request,"ballsuccess.html")
            except Exception as e:
                return render(request,"ballroom.html",{"msg":"sorry there were no ball rooms available"})
    else:
        return redirect("login")

def bookconferenceroom(request):
    if request.session.get("email",None):
        if request.method=="POST":
            try:
                start_date=request.POST["conferencestartdate"]
                end_date=request.POST["conferenceenddate"]
                email=request.session["email"]
                room_type="conference room"
                x=meetingrooms.objects.filter(Q(is_available=True)&Q(room_type=room_type))[0]
                room_no=x.room_no
                x.is_available=False
                x.save()
                z=bookmeetingroommodel(email=email,room_no=room_no,room_type=room_type,start_date=start_date,end_date=end_date)
                z.save()
                return render(request,"consuccess.html")
            except Exception as e:
                print(e)
                return render(request,"conf.html",{"msg":"sorry there were no conference rooms available"})
    else:
        return redirect("login")

def cancelmeetingroom(request,email,roomno,roomtype):
    if request.session.get("email",None):
        x=meetingrooms.objects.get(Q(room_no__iexact=roomno)&Q(room_type__iexact=roomtype))
        x.is_available=True
        x.save()
        bookmeetingroommodel.objects.filter(Q(email__iexact=email)&Q(room_no__iexact=roomno)&Q(room_type__iexact=roomtype)).delete()
        return redirect("mybookings")