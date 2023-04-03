from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import *
from bank_app.models import Banker
from investor_app.models import InvestorsModel
from .forms import *

# Create your views here.

def Business_Home(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    business_data = Business.objects.filter(User=userprofile)
    investor_offers = InvestorsModel.objects.filter(business__in=business_data)
    context = {
        'userprofile': userprofile,
        'business_data': business_data,
        'investor_offers': investor_offers
    }
    return render(request, 'business/Business.html', context)


def delete_business(request, pk):
    idea = Business.objects.get(id=pk)
    idea.delete()
    return redirect('Business_Home')

def business_loan(request):
    bank_loan=Banker.objects.all()
    return render(request,'business/business_loan.html', {'bank_loan':bank_loan})

def Business_Create(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    business_data = Business.objects.all()
    form = BusinessForm(request.POST or None)
    try:
        if form.is_valid():
            business = form.save(commit=False)
            business.User = request.user.userprofile
            business.save()
            return redirect('Business_Home')
    except:
        return HttpResponse("hello")
    context = {
        'one': user,
        'data': userprofile,
        'form': form,
        'business_data': business_data
    }

    return render(request, 'business/Business_profile.html', context)