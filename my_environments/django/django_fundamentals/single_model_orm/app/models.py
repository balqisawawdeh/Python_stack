from django.db import models
    
class users(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    email_address = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(request):
    users.objects.create(f_name=request.POST['firstname'],l_name=request.POST['lastname'],email_address=request.POST['email'],age=request.POST['age'])

def get_all():
    return users.objects.all()

def remove_user(id):
    user= users.objects.last()
    user.delete()
    
    