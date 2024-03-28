from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        'date' : strftime("%Y-%m-%d", gmtime()),
        "teams" : ["AC Milan" , "Real Madrid", "Barcalona"]
    }
 
    return render(request,'index.html', context)

