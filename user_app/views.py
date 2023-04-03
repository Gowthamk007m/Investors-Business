from django.shortcuts import render

from adviser_app.models import Advisors
from business_app.models import Business
from user_app.models import User_Query


# Create your views here.
def User_Home(request):
    business_details = Business.objects.all().order_by('-id')
    advice=Advisors.objects.all()

    context = {'idea': business_details,'advice':advice}
    return render(request, 'user/index.html', context)

def create_query(request, pk):
    business = Business.objects.get(pk=pk)
    user = request.user
    user_profile = user.userprofile
    if request.method == 'POST':
        message = request.POST['message']
        query = User_Query.objects.create(
            user=user_profile,
            Business_name=business,
            message=message,
        )
    return render(request,'user/User_query.html')

