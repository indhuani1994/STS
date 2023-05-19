from django.shortcuts import render
from django.http import HttpResponse
from .form import PlacementForm
from .functions import handle_uploaded_file,photo_uploaded_file
from django.contrib import messages
from .models import Placement_Model


# Create your views here.
def home(request):
    return render(request,"Index.html")
def adminhome(request):
    return render(request,"AdminHome.html")
def placementDetails(request):
    c=Placement_Model.objects.all()

    return render(request,"PlacementDetails.html",{"data":c,"num":0})
def login(request):
    if(request.POST):
        uname=request.POST["txt1"]
        password=request.POST["txt2"]
        mem=request.POST["mem"]
        if(mem=="Admin"):
            print ("Admin")
            if(uname=="Admin" and password=="1234"):
                return render(request,"AdminHome.html")
        elif mem=="Staff":
            print("Staff")
        elif mem=="Student":
            print("Student")
        return render(request,"Index.html")
    return render(request,"Login.html")
def addPlacement(request):
    c=Placement_Model.objects.all()
    d=Placement_Model.objects.all().count()
    form = PlacementForm(request.POST, request.FILES)  
    '''if request.POST :
        #form = PlacementForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            handle_uploaded_file(request.FILES['clogo'])
            photo_uploaded_file(request.FILES['photo'])
            messages.success(request,"Registered Successfully")
            return render(request, "AddPlacement.html", {'form':form})
        else: 
            messages.error(request,"Registered Failed")  
            return render(request, "AddPlacement.html", {'form':form})
    '''
    return render(request,"AddPlacement.html",{'data':c,'count':d,"form":form})
