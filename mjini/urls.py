from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^search/',views.search,name='search'),
    url('profile/$', views.profile, name='profile'),
]