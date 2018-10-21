from django import forms
from .models import *

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        fields = ['profilepic','bio','contact']

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name', 'email']


class AddBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['hood','poster']


class NewHood(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = []