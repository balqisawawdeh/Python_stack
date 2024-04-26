from django.db import models
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Auther(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField()
    notes=models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# def Add_auther_to_book():
#     this_book=Book.objects.get(id=3)
#     this_auther=Auther.objects.get(id=1)
#     this_book.authers.add(this_auther)

def add_auth_to_book(request,book_id):
    if request.POST['auth_id']:
        thisBook = Book.objects.get(id=book_id)
        thisAuthor = Auther.objects.get(id=request.POST['auth_id'])
        thisBook.authers.add(thisAuthor)

#create records for books
def create_book(request):
    title=request.POST['title']
    description=request.POST['description']
    Book.objects.create(title=title,description=description)
#get all Books   
def get_books():
    return Book.objects.all()
#remove book
def remove_book(id):
    book= Book.objects.last()
    book.delete()

#create auther
def create_auther(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    note=request.POST['notes']
    Auther.objects.create(first_name=fname,last_name=lname,notes=note)
#get all Authers   
def get_auther():
    return Auther.objects.all()
#remove auther
def remove_auther(id):
    auther= Auther.objects.last() #instanse of movie i want to update.
    auther.delete()
