from django.shortcuts import render,redirect
from . import models
from .models import User,Show
import bcrypt
def index(request):
    return render(request,"index.html")

def details(request,show_id):
    thisShow = Show.objects.get(id=show_id)
    assoc_users = thisShow.users.all()
    non_assoc_users = User.objects.exclude(shows=thisShow)
    context={
        "thisShow": thisShow,
        "assoc_users": assoc_users,
        "non_assoc_users": non_assoc_users
    }
    return render(request,"show_details.html")

def register(request):
    models.register(request)
    return redirect("/")

def validate_login(request):
    # # models.add_show_to_user(request,user_id)
    # user = User.objects.filter(email=request.POST['user_email']) 
    # if user:
    #     logged_user = user[0]
    #     if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
    #         request.session['user_id'] = logged_user.id
    #         return redirect('/')
    allshows=models.get_shows()
    context = {
    	"all_shows": allshows
    }
    return render(request,"shows.html",context)

def new_show(request):
    models.create_show(request)
    return render(request,"new_show.html")

def edit_show(request):
    models.edit_show(request)
    return render(request,"edit_show.html")