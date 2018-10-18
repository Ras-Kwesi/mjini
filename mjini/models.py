from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to='picture/',blank=True)
    contact = models.CharField(max_length=15,blank=True)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

class Hood(models.Model):
    name = models.CharField(max_length=20)
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



class Business(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    locale = models.ForeignKey(Hood,related_name='location')
    category = models.CharField(max_length=20)