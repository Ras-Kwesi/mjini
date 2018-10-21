from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    if current_user.profile.hood is None:
        hoods = Hood.objects.all()
    else:
        hood_name = current_user.profile.hood


    print(hood_name)
    return render(request,'index.html',{'hood_name':hood_name,'hoods':hoods})



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    hood_name = current_user.profile.hood
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    businesses = Business.objects.filter(owner = current_user)

    return render(request, 'profile.html', {'profile': profile, 'businesses': businesses,
                                            'hood_name':hood_name})


@login_required(login_url='/accounts/login/')
@transaction.atomic
def update(request):
    # current_user = User.objects.get(pk=user_id)
    current_user=request.user
    hood_name = current_user.profile.hood
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
        "profile_form": profile_form,
        'hood_name': hood_name
    })

@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.profile.hood
    # if current_user.profile.hood is None:
    #     return redirect('update')
    # else:
    hood = Post.get_hood_posts(id = hood_id)

    return render(request,'hood.html',{'hood':hood,'hood_name':hood_name})


@login_required(login_url='/accounts/login/')
def choosehood(request):
    return render(request,'choosehood.html')


@login_required(login_url='/accounts/login/')
def business(request,id):
    business = Business.objects.get(id = id)

    return render(request,'business.html',{'business':business,'hood_name':hood_name})



@login_required(login_url='/accounts/login/')
def search(request):
    current_user = request.user
    hood_name = current_user.profile.hood
    if 'business' in request.GET and request.GET["business"]:
        search_query = request.GET.get("business")
        searched_business = Business.get_business(name=search_query)
        print (search_query)
        message = f"{search_query}"
        print(searched_business)

        return render(request, 'search.html',{"message":message,"businesses": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message,
                                              'hood_name': hood_name})

@login_required(login_url='/accounts/login/')
def newbiz(request):
    current_user = request.user
    hood_name = current_user.profile.hood
    if request.method == 'POST':
        addBizForm = AddBusiness(request.POST, request.FILES)
        if addBizForm.is_valid():
            bizform = addBizForm.save(commit=False)
            bizform.owner = current_user
            bizform.locale = current_user.profile.hood
            bizform.save()
        return redirect('index')

    else:
        addBizForm = AddBusiness()
    return render(request, 'add_business.html', {"addBusinessForm": addBizForm,
                                                 'hood_name': hood_name})


@login_required(login_url='/accounts/login/')
def newpost(request):
    current_user = request.user
    hood_name = current_user.profile.hood
    hood = request.user.profile.hood
    if request.method == 'POST':
        newPostForm = NewPost(request.POST, request.FILES)
        if newPostForm.is_valid():
            new_post = newPostForm.save(commit=False)
            new_post.poster = request.user
            new_post.hood = hood
            new_post.save()
        return redirect('index')

    else:
        newPostForm = NewPost()
    return render(request, 'newpost.html', {"newPostForm": newPostForm,
                                            'hood_name': hood_name})


@login_required(login_url='/accounts/login/')
def newhood(request):
    current_user = request.user
    hood_name = current_user.profile.hood
    if request.method == 'POST':
        NewHoodForm = NewHood(request.POST)
        if NewHoodForm.is_valid():
            hoodform = NewHoodForm.save(commit=False)
            # current_user.profile.hoodpin = True
            hoodform.save()
            print('saved')

            # request.session.modified = True
            # current_user.profile.hood = hoodform.id
        # return redirect('profilehood',hoodform.name)
        return redirect('index')


    else:
        NewHoodForm = NewHood()
    return render(request, 'newhood.html', {"newHoodForm": NewHoodForm,
                                            'hood_name': hood_name})


def profilehood(request,name):
    current_user = request.user
    hood_name = current_user.profile.hood
    hoodform = Hood.objects.get(name = name)
    current_user.profile.hood = hoodform.id
    current_user.profile.hoodpin = True

    return redirect('index')