from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=20,unique=True)
    bio = models.CharField(max_length=40,default = '')
    admin = models.ForeignKey(User,related_name='administrate')

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
    hood = models.ForeignKey(Hood,related_name='home',null=True)

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
    poster = models.ForeignKey(User,on_delete=models.CASCADE)


    def save_post(self):
        self.save()

    def remove_post(self):
        self.delete()

    @classmethod
    def get_hood_posts(cls,id):
        posts = Post.objects.filter(id = id)
        return posts

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commentator = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post,related_name='comment',null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_description = models.TextField(max_length=80)
    locale = models.ForeignKey(Hood,related_name='location')
    # category = models.CharField(max_length=20)
    business_number = models.IntegerField(default=0)


    def save_business(self):
        self.save()


    def delete_business(self):
        self.delete()


    @classmethod
    def get_business(cls, name):
        business = Business.objects.filter(name=name)
        return business

    # def update_business(self,id):
