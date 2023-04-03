from django.shortcuts import render, redirect

from accounts.models import UserProfile
from business_app.models import Business
from investor_app.forms import InvestorsForm
from investor_app.models import InvestorsModel


# Create your views here.
def Investors_Home(request):
    business_details = Business.objects.all()
    invest=InvestorsModel.objects.all()
    context = {'idea': business_details,'invest':invest}
    return render(request, 'investor/investor_new.html', context)

def create_Investor_Offer(request,business_id):
    business = Business.objects.get(id=business_id)
    if request.method == 'POST':
        form = InvestorsForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            investor = form.save(commit=False)
            investor.business = business
            investor.User = user_profile
            investor.save()
            return redirect('Investors_Home')
        else:
            print(form.errors)
    else:
        form = InvestorsForm()
    return render(request, 'investor/create_investor_offer.html', {'form': form})