from multiprocessing import context
from token import EXACT_TOKEN_TYPES
from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from bank.models import banks
from bank.models import bankclient


# from .forms import BankForm



# Create your views here.

def home_bank_view(request):
 bankoption=0

 if 'bankOption' in request.GET:
    bankoption= request.GET['bankOption']

    banklist=banks.objects.all()

    if bankoption == "0"  or bankoption == "0#" :
        banklist=banks.objects.all()
        clientlist=bankclient.objects.all()
    else:
       
        clientlist=bankclient.objects.filter(bankid=bankoption)
 else:
    banklist=banks.objects.all()
    clientlist=bankclient.objects.all()

 context= {
    'banklist':banklist,
    'clientlist':clientlist,
    'selectedopt': bankoption
 }
 return render(request,'Banks.html', context)    
   

# def TableSort(request):

#   bank_id= request.Get.get('bankId')

#  return render(request, "banks.html", {'form': form} )   