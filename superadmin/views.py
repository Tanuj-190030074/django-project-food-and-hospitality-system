from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
import datetime
from roombooking.models import bookroommodel
from . models import DineInTables,Rooms,meetingrooms
from . forms import addroomform,addtableform,addmeetingroomform
from django.views.generic import TemplateView
# Create your views here.

def adminhomepage(request):
    bookedcount=[]
    tbookedcount=[]
    bookedcount.append(Rooms.objects.filter(is_available=False).count())
    bookedcount.append(Rooms.objects.filter(is_available=True).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=False).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=True).count())
    return render(request,"adminhome.html",{"bookedcount":bookedcount,"tbookedcount":tbookedcount})

def adminaddroom(request):
    if request.session.get("adminlogin",None):
        if request.method=="POST":
            form=addroomform(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("adminviewrooms")
        else:
            form=addroomform()
        return render(request,"adminaddroom.html",{"form":form})
    else:
        return redirect("loginpage")

def adminaddmeetingroom(request):
    if request.session.get("adminlogin",None):
        if request.method=="POST":
            form=addmeetingroomform(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("adminviewmeetingrooms")
        else:
            form=addmeetingroomform()
        return render(request,"adminaddmeetingroom.html",{"form":form})
    else:
        return redirect("loginpage")


def adminupdateroom(request,roomno):
    if request.session.get("adminlogin",None):
        obj=Rooms.objects.get(room_no=roomno)
        form=addroomform(instance=obj)
        if request.method=="POST":
            form=addroomform(request.POST,request.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("adminviewrooms")
        return render(request,"adminaddroom.html",{"form":form})
    else:
        return redirect("loginpage")

def adminupdatemeetingroom(request,roomno):
    if request.session.get("adminlogin",None):
        obj=meetingrooms.objects.get(room_no=roomno)
        form=addmeetingroomform(instance=obj)
        if request.method=="POST":
            form=addmeetingroomform(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("adminviewmeetingrooms")
        return render(request,"adminaddmeetingroom.html",{"form":form})
    else:
        return redirect("loginpage")

def adminviewrooms(request):
    if request.session.get("adminlogin",None):
        data=Rooms.objects.all().order_by('room_type')
        return render(request,"adminviewrooms.html",{"data":data})
    else:
        return redirect("loginpage")

def adminviewmeetingrooms(request):
    if request.session.get("adminlogin",None):
        data=meetingrooms.objects.all().order_by('room_type')
        return render(request,"adminviewmeetingrooms.html",{"data":data})
    else:
        return redirect("loginpage")

def admindeleteroom(request,roomno):
    if request.session.get("adminlogin",None):
        Rooms.objects.filter(room_no=roomno).delete()
        if bookroommodel.objects.filter(room_no=roomno):
            bookroommodel.objects.filter(room_no=roomno).delete()
        return redirect("adminviewrooms")
    else:
        return redirect("loginpage")

def admindeletemeetingroom(request,roomno):
    if request.session.get("adminlogin",None):
        meetingrooms.objects.filter(room_no=roomno).delete()
        return redirect("adminviewmeetingrooms")
    else:
        return redirect("loginpage")

def adminaddtable(request):
    if request.session.get("adminlogin",None):
        if request.method=="POST":
            form=addtableform(request.POST)
            if form.is_valid():
                form.save()
                return redirect("adminviewtables")
        else:
            form=addtableform()
        return render(request,"adminaddtable.html",{"form":form})
    else:
        return redirect("loginpage")

def adminviewtables(request):
    if request.session.get("adminlogin",None):
        data=DineInTables.objects.all()
        return render(request,"adminviewtables.html",{"data":data})
    else:
        return redirect("loginpage")

def adminupdatetable(request,tableno):
    if request.session.get("adminlogin",None):
        obj=DineInTables.objects.get(table_no=tableno)
        form=addtableform(instance=obj)
        if request.method=="POST":
            form=addtableform(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("adminviewtables")
        return render(request,"adminaddtable.html",{"form":form})
    else:
        return redirect("loginpage")

def admindeletetable(request,tableno):
    if request.session.get("adminlogin",None):
        DineInTables.objects.filter(table_no=tableno).delete()
        return redirect("adminviewtables")
    else:
        return redirect("loginpage")

def chartsdata(request):
    data = []
    data4=[]
    data3=[]
    tbookedcount=[]
    data.append(Rooms.objects.filter(is_available=False).count())
    data4.append(DineInTables.objects.filter(is_available=False).count())
    data4.append(Rooms.objects.filter(Q(is_available=False)&Q(room_type="king guestroom")).count())
    data4.append(Rooms.objects.filter(Q(is_available=False)&Q(room_type="king deluxe guestroom")).count())
    data4.append(Rooms.objects.filter(Q(is_available=False)&Q(room_type="twin guestroom")).count())
    data4.append(meetingrooms.objects.filter(Q(is_available=False)&Q(room_type="ball room")).count())
    data4.append(meetingrooms.objects.filter(Q(is_available=False)&Q(room_type="conference room")).count())
    data3.append(meetingrooms.objects.filter(Q(is_available=False)&Q(room_type="ball room")).count())
    data3.append(meetingrooms.objects.filter(Q(is_available=False)&Q(room_type="conference room")).count())
    data.append(Rooms.objects.filter(is_available=True).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=False).count())
    tbookedcount.append(DineInTables.objects.filter(is_available=True).count())
    
    return JsonResponse(data={
        'labels': ["booked","available"],
        'labels2':["Table Bookings","king guestroom Bookings","king deluxe guestroom Bookings","twin guestroom Bookings","ball room Bookings","Conference room Bookings"],
        'labels3':["Ball Room Bokkings","Conference room bookings"],
        'data': data,
        'data3':data3,
        'data2':tbookedcount,
        'data4':data4,
    })
def adminoptimizetablespage(request):
    return render(request,"adminoptimizetables.html")

def adminoptimizetables(request):
    if request.method=="POST":
        def firstFit(weight, n, c):
            # Initialize result (Count of bins)
            res = 0;
            bin_rem = [0]*n;
            for i in range(n):
                j = 0;
                min = c + 1;
                bi = 0;
                for j in range(res):
                    if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                        bi = j;
                        min = bin_rem[j] - weight[i];
                if (min == c + 1):
                    bin_rem[res] = c - weight[i];
                    res += 1;
                else: 
                    bin_rem[bi] -= weight[i];
            return res;
        weight = request.session["saved2"];
        print(request.session["saved2"])
        c = int(request.POST["capacity"]);
        n = len(weight);
        mb=firstFit(weight, n, c)
        return render(request,"adminoptimizetables.html",{"msg":mb})
