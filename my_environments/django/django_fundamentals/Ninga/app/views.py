# from django.shortcuts import render, redirect
# import 	datetime
# import random

# def index(request):
#     if "gold" not in request.session:
#         request.session["gold"]=0
#     if "activities" not in request.session:
#          request.session["activities"]=[]
#     return render(request,"index.html")

# def process(request):
#     if request.method=='POST':
#         building=request.POST['building']
#         if building =='farm':
#             earn=random.randint(10,20)
#             request.session['gold'] += earn
#             request.session['activities'].append(f'Earned {earn} golds at the farm! ({datetime.datetime.now()})')
#         elif building =='cave':
#             earn=random.randint(10,20)
#             request.session['gold'] += earn
#             request.session['activities'].append(f'Earned {earn} golds at the cave! ({datetime.datetime.now()})') 
#         elif building =='house':
#             earn=random.randint(10,20)
#             request.session['gold'] += earn
#             request.session['activities'].append(f'class="green" Earned {earn} golds at the house! ({datetime.datetime.now()})')
#         elif building == 'cafeteria':
#             earn = random.randint(-50, 50)
#             request.session['gold'] += earn
#             if request.session['gold']>0:
#                 request.session['activities'].append(f'Entered a casino and win {earn} golds...({datetime.datetime.now()})')
#             else:
#                 request.session['activities'].append(f'class="red" Entered a casino and lost {earn} golds... ouch.. ({datetime.datetime.now()})')
                
#         return redirect('/')

# def destroy(request):
#     return redirect("/")    
from django.shortcuts import render, redirect
import datetime
import random
 
def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    if "activities" not in request.session:
         request.session["activities"]=[]
    return render(request,"index.html")
 
def process(request):
    if request.method=='POST':
        building=request.POST['building']
        if building =='farm':
            earn=random.randint(10,20)
            request.session['gold'] += earn
            request.session['activities'].append({'class':'green', 'activity':f'Earned {earn} golds at the farm! ({datetime.datetime.now()})'})
        elif building =='cave':
            earn=random.randint(10,20)
            request.session['gold'] += earn
            request.session['activities'].append({'class':'green', 'activity':f'Earned {earn} golds at the cave! ({datetime.datetime.now()})'})
        elif building =='house':
            earn=random.randint(10,20)
            request.session['gold'] += earn
            request.session['activities'].append({'class':'green', 'activity':f'class="green" Earned {earn} golds at the house! ({datetime.datetime.now()})'})
        elif building == 'cafeteria':
            earn = random.randint(-50, 50)
            request.session['gold'] += earn
            if earn>0:
                request.session['activities'].append({'class':'green', 'activity':f'Entered a casino and win {earn} golds...({datetime.datetime.now()})'})
            else:
                request.session['activities'].append({'class':'red', 'activity':f'Entered a casino and lost {earn} golds... ouch.. ({datetime.datetime.now()})'})
        return redirect('/')
 
def destroy(request):
    return redirect("/")
