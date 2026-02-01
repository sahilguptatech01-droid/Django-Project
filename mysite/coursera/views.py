from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Course
from .forms import AddForm






# Create your views here.

def home_page(request):
    items=Course.objects.all()
    return render(request,'coursera/home.html',{'items':items})

def detail(request,id):
    items=Course.objects.get(id=id)
    return render(request,"coursera/detail.html",{"items":items})


def add_course(request):
    form=AddForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("coursera:home")
    else:
        form=AddForm()
        

   
    return render(request,'coursera/add_form.html',{"form":form})


def buy(request):
    return render(request,'coursera/buy.html')


def delete_course(request,id):
    item=Course.objects.get(id=id)
    
    if request.method=="POST":
        item.delete()
        return redirect('coursera:home')

    return render (request,'coursera/delete.html')


    
    

