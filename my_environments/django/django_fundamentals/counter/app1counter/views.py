from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return render(request, "index.html")

def addtwo(request):
    request.session['counter']+=2
    return render(request, "index.html")

def reset(request):
    request.session.clear()
    return redirect('/')
