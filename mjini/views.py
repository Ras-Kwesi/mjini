from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *



# Create your views here.
def index(request):


    return render(request,'index.html')



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    businesses = Business.objects.filter(owner = current_user)

    return render(request, 'profile.html', {'profile': profile, 'businesses': businesses})


@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    hood = Hood.get_hood(id = hood_id)

    return render(request,'hood.html')

@login_required(login_url='/accounts/login/')
def search(request):

    if 'business' in request.GET and request.GET["business"]:
        search_query = request.GET.get("business")
        searched_business = Business.get_business(name=search_query)
        print (search_query)
        message = f"{search_query}"
        print(searched_business)

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

