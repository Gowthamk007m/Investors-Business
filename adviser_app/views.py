from django.shortcuts import render, redirect
from business_app.models import Business

from accounts.models import UserProfile
from adviser_app.models import Advisors
from user_app.models import User_Query


def see_business(request):
    business_details = Business.objects.all().order_by('-id')
    advice = Advisors.objects.all()

    context = {'idea': business_details, 'advice': advice}
    return render(request, 'adviser/ideas.html', context)

# Create your views here.
def advisor_home(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    advisor = Advisors.objects.filter(advisor_name=userprofile)
    query = User_Query.objects.all()
    context = {'query': query}
    return render(request, 'adviser/advisor_home.html', context)


def create_reply(request, pk):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    advisor = Advisors.objects.filter(advisor_name=userprofile)
    query_data = User_Query.objects.get(id=pk)

    if request.method == 'POST':
        advice = request.POST['advice']
        query = Advisors.objects.create(
            query=query_data,
            advisor_name=userprofile,
            advice=advice,
        )
        return redirect('advisor_home')

    return render(request, 'adviser/advice_user.html')
