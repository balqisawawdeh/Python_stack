from django.db import models
import bcrypt
import re

#regular Exp:
class UserManager(models.Manager):
    def user_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z0-9.+_-]+$')
        if len(postData['fname'])<2:
            errors["fname"]="first name should be at least 2 characters"
            return errors
        if len(postData['lname'])<2:
            errors["lname"]="first name should be at least 2 characters"
            return errors
        if len(postData['password'])<2:
            errors["password"]="Password should be at least 8 characters"
            return errors
        if not EMAIL_REGEX.match(postData['user_email']):
            errors['user_email'] = "Invalid email address!"
            return errors
        conf_field=postData['password']
        if not conf_field.match(postData['conf_pw']):
            errors['conf_pw'] = "password does not matched!"
            return errors
# Create User model here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.TextField()
    conf_pw=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create show model here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    comments=models.CharField(max_length=255)
    releas_date=models.DateTimeField()
    users = models.ManyToManyField(User, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# add show to user
def add_show_to_user(request,user_id):
    if request.POST['show_id']:
        thisUser = User.objects.get(id=user_id)
        thisShow = Show.objects.get(id=request.POST['show_id'])
        thisUser.shows.add(thisShow)

#create new user
def register(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    rg_email=request.POST['user_email']
    password=request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    confirm_pw=request.POST['conf_pw']
    User.objects.create(first_name=fname,last_name=lname,email=rg_email,password=pw_hash,conf_pw=confirm_pw)

#create show
def create_show(request):
    s_title=request.POST['new_title']
    s_network=request.POST['network']
    s_release_date=request.POST['release_date']
    s_comment=request.POST['comment']
    Show.objects.create(title=s_title,network=s_network,releas_date=s_release_date,comments=s_comment)

def edit_show(request,show_id):
    update_show=Show.objects.get(id=show_id)
    e_title=request.POST['edit_title']
    e_title=request.POST['edit_network']
    e_release_date=request.POST['edit_release_date']
    e_comment=request.POST['edit_comment']
    update_show.save()

def get_shows():
    return Show.objects.all()