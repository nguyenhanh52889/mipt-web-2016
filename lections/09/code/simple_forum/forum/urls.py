from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^thread/(?P<thread_id>\d+)/(?P<page_num>\d+)/$', views.thread, name='thread'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),
    url(r'^send_message/(?P<thread_id>\d+)/$', views.send_message, name='send_message'),
    url(r'^register/$', views.register, name='register'),
    url(r'^load_messages/$', views.load_messages, name='load_messages'),
]
