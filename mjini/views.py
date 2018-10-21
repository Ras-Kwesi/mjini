from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from .forms import *


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
@transaction.atomic
def update(request):
    # current_user = User.objects.get(pk=user_id)
    current_user=request.user
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES,instance=request.user)
        profile_form = EditProfile(request.POST, request.FILES,instance=current_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
        return redirect('profile')

    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=current_user.profile)
    return render(request, 'update_profile.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })

@login_required(login_url='/accounts/login/')
def hood(request,hood_name):
    hood = Post.get_hood_posts(hood_name = hood_name)

    return render(request,'hood.html',{'hood':hood})

@login_required(login_url='/accounts/login/')
def search(request):

    if 'business' in request.GET and request.GET["business"]:
        search_query = request.GET.get("business")
        searched_business = Business.get_business(name=search_query)
        print (search_query)
        message = f"{search_query}"
        print(searched_business)

        return render(request, 'search.html',{"message":message,"businesses": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_biz(request):
    current_user = request.user
    if request.method == 'POST':
        addBizForm = AddBusiness(request.POST, request.FILES, instance=request.user)
        if addBizForm.is_valid():
            bizform = addBizForm.save(commit=False)
            bizform.owner = current_user
            bizform.save()
        return redirect('index')

    else:
        addBizForm = AddBusiness(instance=request.user,)
    return render(request, 'add_business.html', {"addBusinessForm": addBizForm})


@login_required(login_url='/accounts/login/')
def newpost(request):
    current_user = request.user
    hood = request.user.hood
    if request.method == 'POST':
        newPostForm = NewPost(request.POST, request.FILES, instance=request.user)
        if newPostForm.is_valid():
            new_post = newPostForm.save(commit=False)
            new_post.poster = current_user
            new_post.hood = hood
            new_post.save()
        return redirect('index')

    else:
        newPostForm = NewPost(instance=request.user)
    return render(request, 'newpost.html', {"newPostForm": newPostForm})
