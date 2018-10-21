from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^search/',views.search,name='search'),
    url('profile/$', views.profile, name='profile'),
    url('^hood/(\w+)', views.hood, name='hood'),
    url('^update/$', views.update, name='update'),
    url('^addbiz/$', views.newbiz, name='addbiz'),
    url('^newpost/$', views.newpost, name='newpost'),
    url('^newhood/$', views.newhood, name='newhood'),
    url('^profilehood/(\w+)$', views.profilehood, name='profilehood'),
    url('^choosehood/$',views.choosehood,name='choosehood'),

]