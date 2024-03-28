from django.shortcuts import render
from .models import User
from app import models


def index(request):
    context = {
    	"all_the_users": User.objects.all()
    }
    return render(request,'index.html',context)

def create(request):
    models.create_user()
    return render(request,'index.html')