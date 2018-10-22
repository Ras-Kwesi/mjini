from django import forms
from .models import *

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        fields = ['profilepic','bio','contact','hood']

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        fields = ['first_name','last_name', 'email']


class AddBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner','locale']


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['hood', 'poster']


class NewHood(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ['name', 'bio']


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['commentator','comment_post']