from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'Ras_Kwesi', email = 'ras@ras.com', password = 'passwadd')
        self.user.save()
        self.ras = Profile(bio = 'A python Programmer',contact = '054234444', user = self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ras,Profile))

    def test_save(self):
        self.ras.create_user_profile(self.user,True)
        self.ras.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users)>0)


class HoodTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.user.save()
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name = 'Ngong',bio = "Milimani",admin = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Hood))

    def test_save(self):
        self.hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 1)
