from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")


def result(request):
    Name = request.POST['name']
    location = request.POST['location']
    language=request.POST['language']
    comment=request.POST['comment']

    context={
        'Name':Name,
        'location':location,
        'language':language,
        'comment':comment
    }
    return render(request,'results.html',context)