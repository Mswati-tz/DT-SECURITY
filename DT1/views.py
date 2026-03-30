from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

#hizi za message ile def ya mwisho apo chini
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage



# Create your views here.

def home(request):
    updates = models.Update.objects.all().order_by('-id')[:5] 
    return render(request, 'home.html', {'update': updates})
    

def about(request):
    return render(request,'about.html')




def services(request):
    service_all = models.Service.objects.all().order_by('-created_at') 
    
    paginator = Paginator(service_all, 3) # Huduma 3 kwa kila ukurasa
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    # HAPA: Hakikisha umeandika 'context'
    return render(request, 'services.html', context)





 def client(request):
    # Tunachukua wateja wote kutoka Admin/Database
    all_clients = Client.objects.all() 
    
    # MUHIMU: Jina hapa kushoto ('clients') lazima lifanane na lile la kwenye HTML loop
    context = {
        'clients': all_clients,
    }
    return render(request, 'client.html', context)
    #return render(request,'our_clients.html')




def update(request):
    updates=models.Update.objects.all().order_by('-id')[:5]
    return render(request,'updates.html',{'update':updates})

def contact(request):
    return render(request,'contact.html')

def apply(request):
    return render(request,'apply.html')




def contact(request):
    if request.method == 'POST':
        # 1. Chukua data kutoka kwenye fomu ya HTML
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # 2. Hakikisha data muhimu zipo kabisa kabla ya kusave
        if name and email and message:
            # Save kwenye Database (Model ya ContactMessage)
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Toa ujumbe wa mafanikio (Success Message)
            messages.success(request, 'Ujumbe wako umetumwa kikamilifu! Tutakujibu hivi punde kupitia email yako.')
            
            # Inarudisha mteja kwenye page ya contact akiwa amesafishiwa fomu
            return redirect('contact')
        else:
            # Ikijitokeza mteja ameacha wazi sehemu muhimu
            messages.error(request, 'Tafadhali jaza nafasi zote zinazohitajika.')

    # Hii inafungua ukurasa wa mawasiliano kama mteja hajabonyeza "Send"
    return render(request, 'contact.html')




