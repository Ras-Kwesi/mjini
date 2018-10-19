from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^search/',views.search,name='search'),
    url('profile/$', views.profile, name='profile'),
    # url('^new_post/', views.new_post, name='new_post'),
    url('update/$', views.update, name='update'),
    url('addbiz/$', views.new_biz, name='addbiz'),

]