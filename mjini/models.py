from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=20,unique=True)
    residents = models.IntegerField(default=1)
    county = models.CharField(max_length=20)

    def save_hood(self):
        self.save()

    def remove_hood(self):
        self.delete()


    @classmethod
    def get_hood(cls,id):
        hood = Hood.objects.get(id=id)
        return hood



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to='picture/',blank=True)
    contact = models.CharField(max_length=15,blank=True)
    hoodpin = models.BooleanField(default=False)
    hood = models.ForeignKey(Hood,related_name='home')

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

# class Hood(models.Model):
#     name = models.CharField(max_length=20,unique=True)
#     residents = models.IntegerField(default=1)
#     county = models.CharField(max_length=20)
#
#     def save_hood(self):
#         self.save()
#
#     def remove_hood(self):
#         self.delete()
#
#
#     @classmethod
#     def get_hood(cls,id):
#         hood = Hood.objects.get(id=id)
#         return hood

class Post(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField(max_length=100)
    hood = models.ForeignKey(Hood,related_name='hood')
    poster = models.ForeignKey(User,related_name='poster')

    @classmethod
    def get_hood_posts(cls,hood_name):
        posts = Post.objects.filter(hood__name = hood_name )
        return posts

class Business(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_description = models.TextField(max_length=80)
    locale = models.ForeignKey(Hood,related_name='location')
    # category = models.CharField(max_length=20)
    business_number = models.IntegerField(default=0)

    def save_business(self):
        self.save()

    @classmethod
    def get_business(cls, name):
        business = Business.objects.get(name=name)
        return business