from django.db import models
    
class User(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    email_address = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user():
    new_user=User.objects.create(f_name="Chidi",l_name="Anagonye",email_address="chidi@angonye.com",age=32)

def get_all():
    all_users = User.objects.all()
    