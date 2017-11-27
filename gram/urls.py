from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views


urlpatterns =[
  url(r'^$', views.index, name='Home'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
  url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
  url(r'^post/$', views.posts, name='post_picture'),
]