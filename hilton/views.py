from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from roombooking.models import registrationmodel
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from food.models import bookdineinmodel
from superadmin.models import DineInTables
from roombooking.models import bookroommodel
from tablebooking.models import bookmeetingroommodel
from superadmin.models import Rooms,superadminlogin,meetingrooms
from django.contrib.auth.hashers import make_password,check_password

def indexfunction(request):
    return render(request,"index.html")

def registrationpage(request):
    return render(request,"registration.html")

def loginpage(request):
    return render(request,"login.html")

def foodpage(request):
    return render(request,"food.html")

def dineinpage(request):
    if request.session.get("email",None):
        print(request.session["email"])
        return render(request,"dinein.html")
    else:
        return redirect("loginpage")

def register(request):
    if request.method=="POST":
        try:
            firstname=request.POST["firstname"]
            lastname=request.POST["lastname"]
            email1=request.POST["email"]
            password=request.POST["password"]
            passsword=make_password(password)
            mobile=request.POST["mobile"]
            address1=request.POST["add1"]
            address2=request.POST["add2"]
            city=request.POST["city"]
            state=request.POST["state"]
            zipcode=request.POST["zipcode"]
            data=registrationmodel(firstname=firstname,lastname=lastname,email=email1,password=passsword,mobile=mobile,address1=address1,address2=address2,city=city,state=state,zipcode=zipcode)
            data.save()
            subject="Hilton Registration"
            email=email1 #to whom you want to send
            email=EmailMessage(subject,"Dear User,\n\nWelcome to Hilton.\n you are succesfully registered in our website and we are happy to serve you anyday.\nThank you",to=[email])
            email.send()
            return redirect("success")
        except Exception as e:
            print(e)
            return render(request,"registration.html",{'msg':"email already taken"})
def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        if registrationmodel.objects.filter(email=email).all() and check_password(password,registrationmodel.objects.get(email=email).password):
            x=registrationmodel.objects.get(email=email)
            request.session["email"]=email
            request.session["name"]=x.firstname
            print(x.firstname)
            return redirect("indexfunction")
        elif superadminlogin.objects.filter(email__iexact=email).all() and check_password(password,superadminlogin.objects.get(email=email).password):
            request.session["adminlogin"]="true"
            return redirect("adminhomepage")
        else:
            return render(request,"login.html",{"err":"True"})

def success(request):
    return render(request,"rsuccess.html")

def logout(request):
    del request.session["email"]
    del request.session["name"]
    return redirect("indexfunction")

def roombookingpage(request):
    if request.session.get("email",None):
        print(request.session["email"])
        return render(request,"kgbook.html")
    else:
        return redirect("loginpage")

def mybookings(request):
    if request.session.get("email",None):
        print(request.session["email"])
        dineinbookings=bookdineinmodel.objects.filter(email=request.session["email"])
        bookrooms=bookroommodel.objects.filter(email=request.session["email"])
        bookmeetingrooms=bookmeetingroommodel.objects.filter(email=request.session["email"])
        totalbookroom=0
        for j in bookrooms:
            totalbookroom=totalbookroom+j.price
        return render(request,"mybookings.html",{"dineinbookings":dineinbookings,"bookrooms":bookrooms,"bookmeetingrooms":bookmeetingrooms,"totalbookroom":totalbookroom})
    else:
        return redirect("loginpage")

def adminlogout(request):
    del request.session["adminlogin"]
    return redirect("indexfunction")
