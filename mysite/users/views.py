from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout


# Create your views here.

def register(request):
    form=RegisterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Weclome {username}")
            return redirect("coursera:home")


    else:
       form=RegisterForm()

    return render(request,'users/register.html',{"form":form})


    
def logout_view(request):
    logout(request)
    
    return render(request,'users/logout.html')




