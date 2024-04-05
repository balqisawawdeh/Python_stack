from django.shortcuts import render, redirect
from . import models

def index(request):
    alldojos=models.get_dojo()
    Allninjas=models.get_ninja()
    context = {
    	"Alldojos": alldojos,
        "Allninjas":Allninjas
    }
    return render(request,'index.html',context)

#create new dojo
def create_dojo(request):
    models.create_dojo(request)
    return redirect('/')

#get all dojos
def getalldojo(request):
    context={'Alldojos':models.get_dojo()}
    return render(request,"index.html",context)

#create new ninja
def addninjas(request):
    models.addninjas(request)
    return redirect('/')

#get all Ninjas   
def getallninjas(request):
    context={'Allninjas':models.get_ninja()}
    return render(request,"index.html",context)