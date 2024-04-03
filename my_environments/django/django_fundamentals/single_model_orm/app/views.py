from django.shortcuts import render,redirect
from . import models

def index(request):
    allusers=models.get_all()
    context = {
    	"all_the_users": allusers
    }
    return render(request,'index.html',context)

def create(request):
    models.create_user(request)
    return redirect('/')

def remove(request):
    models.remove_user(id=id)
    return redirect('/')