from django.db import models
    
class dojos(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc=models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ninjas(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(dojos, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)