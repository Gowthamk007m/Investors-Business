from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.models import Group


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def register(request, pk):
    user = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pancard = form.cleaned_data.get('pan_card')
            aadhaar = form.cleaned_data.get('aadhaar')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            user = form.save()
            user_profile = UserProfile.objects.create(
                user=user,
                name=username,
                pancard_number=pancard,
                aadhaar_number=aadhaar,
                email=email,
                phone=phone,
            )
            user_profile.save()
    else:
        form = CreateUserForm()

    group_mapping = {
        1: 'users',
        2: 'Business people',
        3: 'advisors',
        4: 'investors',
        5: 'bankers',

    }

    if pk in group_mapping and user:
        group_name = group_mapping[pk]
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        user.save()

        return redirect('login')

    context = {'form': form}

    return render(request, 'main/reg.html', context)


def Login_page(request):

    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        user = authenticate(request, identifier=identifier, password=password)
        if user is not None:
            login(request, user)

            if user.groups.filter(name='users').exists():
                return redirect('User_Home')
            elif user.groups.filter(name='Business people').exists():
                return redirect('Business_Home')
            elif user.groups.filter(name='investors').exists():
                return redirect('Investors_Home')

            elif user.groups.filter(name='bankers').exists():
                return redirect('bankers_home')
            elif user.groups.filter(name='advisors').exists():
                return redirect('advisor_home')
        else:

            messages.info(request, 'try again')

    context = {'messages': messages}

    return render(request, 'main/login1.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('login')
