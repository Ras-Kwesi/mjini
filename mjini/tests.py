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


class BusinessTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.user.save()
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name='Ngong', bio="Milimani", admin=self.user)
        self.business = Business(name="Murugu", owner = self.user, business_description= 'Herbal',
                                 locale = self.hood,business_number = 4322323)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()
        self.business.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save(self):
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 1)


class PostTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.user.save()
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name='Ngong', bio="Milimani", admin=self.user)
        self.business = Business(name="Murugu", owner = self.user, business_description= 'Herbal',
                                 locale = self.hood,business_number = 4322323)
        self.post = Post(title='Postings',post = 'This is the post',
                         hood = self.hood, poster = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()
        self.business.delete()
        self.post.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 1)

class CommentTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.user.save()
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name='Ngong', bio="Milimani", admin=self.user)
        self.business = Business(name="Murugu", owner = self.user, business_description= 'Herbal',
                                 locale = self.hood,business_number = 4322323)
        self.post = Post(title='Postings', post='This is the post',
                         hood=self.hood, poster=self.user)
        self.comment = Comment(comment = 'comment',commentator = self.user,comment_post = self.post)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()
        self.business.delete()
        self.post.delete()
        self.comment.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment))

    def test_save(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(1)== 1)