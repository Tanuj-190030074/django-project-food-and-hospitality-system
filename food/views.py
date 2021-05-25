from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
import datetime
from superadmin.models import DineInTables
from . models import bookdineinmodel

def bookdinein(request):
    if request.session.get("email",None):
        if request.method=="POST":
            try:
                if not 'saved2' in request.session or not request.session['saved2']:
                    request.session['saved2'] = []
                saved_list = request.session['saved2']
                saved_list.append(int(request.POST["number_people"]))
                request.session['saved2'] = saved_list
                print(request.session["saved2"])
                time=request.POST["time"]
                space=request.POST["number_people"]
                email=request.session["email"]
                x=DineInTables.objects.filter(Q(is_available=True)&Q(capacity__gte=space))[0]
                table_no=x.table_no
                x.is_available=False
                x.save()
                y=bookdineinmodel(email=email,table_no=table_no,time=time,space=space)
                y.save()
                return render(request,"dsuccess.html")
            except Exception as e:
                return render(request,"dinein.html",{"msg":"sorry there were no tables available"})
    else:
        return redirect("login")

def canceldinein(request,email,tableno):
    if request.session.get("email",None):
        x=DineInTables.objects.get(table_no=tableno)
        x.is_available=True
        x.save()
        bookdineinmodel.objects.filter(Q(email__iexact=email)&Q(table_no__iexact=tableno)).delete()
        return redirect("mybookings")