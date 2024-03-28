from django.shortcuts import render,redirect
import random
 
def index(request):
    number = random.randint(1, 10)
    request.session['number'] = number
    request.session['attempts'] = 0
    context={
        'number':number
    }
    return render(request,'index.html',context)

def guess(request):
    if request.method == 'POST':
        session_number=request.session['number']
        secret_number=request.POST['number']
        if int(secret_number)==int(session_number):
            request.session['message']='win'
        elif int(secret_number)>int(session_number):
            request.session['message']='high'
        elif int(secret_number)<int(session_number):
            request.session['message']='low'
        request.session['attempts']+=1
        return render(request,'index.html')

def attempts(request):        
    if request.session['message']!='win' and request.session['attempts']== 5:
        request.session['message'] ='lose'
    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')