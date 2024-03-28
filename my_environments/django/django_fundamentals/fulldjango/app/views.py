from django.shortcuts import render

from app import models

def index(request):
    #models.create_movie()
    #models.update_movie(id=1)
    models.remove_movie(id=2)
    return render(request,"index.html")