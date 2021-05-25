from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
import datetime
from . models import bookroommodel
from superadmin.models import Rooms

def searchrooms(request):
    if request.method=="POST":
        startdate=request.POST["startdate"]
        enddate=request.POST["enddate"]
        request.session["startdate"]=startdate
        request.session["enddate"]=enddate
        roomtype=request.POST["roomtype"]
        data=Rooms.objects.filter(Q(is_available=True)&Q(room_type__iexact=roomtype)).order_by('price')
        if data:
            return render(request,'searchrooms.html',{'data':data})
        else:
            return render(request,'Kgbook.html',{'nodata':True})

def bookroom(request,roomno,roomtype,price):
    prices=[]
    price1=float(price)
    x=Rooms.objects.get(room_no=roomno)
    x.is_available=False
    x.bookcount=x.bookcount+1
    x.save()
    email=request.session["email"]
    start_date=request.session["startdate"]
    end_date=request.session["enddate"]
    prices.append(price1)
    y=bookroommodel(email=email,room_no=roomno,room_type=roomtype,price=price1,start_date=start_date,end_date=end_date)
    y.save()
    del request.session["startdate"]
    del request.session["enddate"]
    return redirect("mybookings")

def cancelroom(request,email,roomno):
    x=Rooms.objects.get(room_no=roomno)
    x.is_available=True
    x.bookcount=x.bookcount-1
    x.save()
    if bookroommodel.objects.filter(Q(email__iexact=email)&Q(room_no__iexact=roomno)).delete():
        return redirect("mybookings")
    else:
        return HttpResponse("try again")

def roomview(request,roomno):
    data=Rooms.objects.filter(room_no=roomno)[0]
    print(data)
    return render(request,"singlepage.html",{'data':data})

def singlepage(request):
    return render(request,"singlepage.html")

def psuccess(request):
    return render(request,"psuccess.html")

def paymentcompleted(request):
    booked=Rooms.objects.filter(is_available=False)
    for i in booked:
        i.is_available=True
        i.save()
    bookroommodel.objects.all().delete()
    return redirect("psuccess")
