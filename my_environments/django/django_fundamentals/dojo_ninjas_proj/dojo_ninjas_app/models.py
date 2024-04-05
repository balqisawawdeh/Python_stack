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
    dojos.objects.create(Name=request.POST.get('Name'),city=request.POST.get('city'),state=request.POST.get('state'))

#get all dojos   
def get_dojo():
    return dojos.objects.all()

#create new Ninja
def addninjas(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        dojo=dojos.objects.get(id=request.POST['FRdojo'])
        ninjas.objects.create(f_name=fname,l_name=lname,dojo=dojo)

#get all Ninjas   
def get_ninja():
    return ninjas.objects.all()