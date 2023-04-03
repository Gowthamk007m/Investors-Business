from django.shortcuts import render, redirect

from accounts.models import UserProfile
from bank_app.forms import BankerForm
from bank_app.models import Banker


# Create your views here.

def bankers_home(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    bankdata = Banker.objects.filter(banker=userprofile)
    context = {'bankdata': bankdata}
    return render(request,'bank/Banker.html', context)


def create_bank_loan(request):

    if request.method == 'POST':
        form = BankerForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            investor = form.save(commit=False)
            investor.banker = user_profile
            investor.save()

            return redirect('bankers_home')
    else:
        form = BankerForm()

    return render(request, 'bank/bank_form.html', {'form': form})
