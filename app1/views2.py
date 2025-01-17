from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student



def index(request):
    data=Student.objects.get.all()
    print(data)
    context={'data':data}
    return render(request,'index.html',context)

def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data inserted Succesfully")
        return redirect("/")
    
    return render(request,'index.html')

def update(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.name=email
        edit.name=age
        edit.name=gender
        edit.save()
        messages.info(request,"data update succesfully")
        return redirect("/")

    d=Student.objects.get(id=id)
    context={'d':d}
    return render(request,"edit.html",context)

def deletedata(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.info(request,"data deleted")
    return redirect("/")
