
from django.shortcuts import render,HttpResponse

# Create your views here.
##def Home(request):
    ##return HttpResponse("Halaman Home")
    
def home(request):
    context={
        
    }
    return render(request, 'home.html',context)

def profil(request):
    context={
        
    }
    return render(request, 'profil.html',context)

def contact(request):
    context={
        
    }
    return render(request, 'contact.html',context)