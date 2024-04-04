from django.db import models
    
#Initiate dojos class
class dojos(models.Model):
    Name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc=models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Initiate ninjas class
class ninjas(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(dojos, related_name="Ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#create new dojo
def create_dojo(request):
    dojos.objects.create(Name=request.POST['Name'],city=request.POST['city'],state=request.POST['state'])
    print(request.POST)

#get all dojos   
def get_dojo():
    return dojos.objects.all()

#create new Ninja
def create_Ninja(request):
    ninjas.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],dojo=dojos.objects.get(id=2))

#get all Ninjas   
def get_ninja():
    return ninjas.objects.all()