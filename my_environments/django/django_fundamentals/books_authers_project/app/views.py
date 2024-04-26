from django.shortcuts import render, redirect
from . import models
from .models import Book,Auther
#return main page
def index(request):
    allbooks=models.get_books()
    context = {
    	"all_books": allbooks
    }
    return render(request,"index.html",context)

#----book functions----#
def create_book(request):
    models.create_book(request)
    return redirect('/')

def remove_book(request):
    models.remove_book(id=id)
    return redirect('/')

def view_book(request,book_id):
    thisBook = Book.objects.get(id=book_id)
    assoc_authers = thisBook.authers.all()
    non_assoc_authers = Auther.objects.exclude(id__in=assoc_authers.values_list("id"))
    data = {
        "thisBook": thisBook,
        "assoc_authers": assoc_authers,
        "non_assoc_authers": non_assoc_authers
    }
    print(assoc_authers)
    print(non_assoc_authers)
    return render(request, "sub_book.html",data)

def add_auth_to_book(request,book_id):
    models.add_auth_to_book(request,book_id)
    return redirect("/")
#----End of book functions----#

#----Auther functions----#
def auther(request,book_id):
    models.Add_auther_to_book(request,id=book_id)
    allauthers=models.get_auther()
    context = {
    	"all_authers": allauthers
    }
    return render(request,"auther.html",context)

def create_auther(request):
    models.create_auther(request)
    return redirect('/authers')

def remove_auther(request):
    models.remove_auther(id=id)
    return redirect('/authers')
#return auther details page
def view_auther(request,auther_id):
    thisAuther = Auther.objects.get(id=auther_id)
    assoc_books = thisAuther.books.all()
    non_assoc_books = Book.objects.exclude(authers=thisAuther)
    data = {
        "thisAuther": thisAuther,
        "assoc_books": assoc_books,
        "non_assoc_books": non_assoc_books
    }
    return render(request, "sub_auther.html")


# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# @app.route('/dojo')
# def dojo():
#     return "Dojo!"

# @app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def say(name):
#     print(name)
#     return "Hi, " + name

# @app.route("/repeat/<int:x>/<word>")
# def repeat_word(x, word):
#     repeated_word = word * x
#     return repeated_word


# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.


