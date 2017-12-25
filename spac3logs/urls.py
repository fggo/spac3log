from django.conf.urls import url

from . import views

app_name = 'spac3logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # topics
    url(r'^topics/$', views.topics, name='topics'),
    # topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # new topic
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # new entry
    # url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,
    #     name='new_entry'),
    # edit entry
    # url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    #     name='edit_entry'),
]