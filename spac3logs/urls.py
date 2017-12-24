from django.conf.urls import url

from . import views

app_name = 'spac3logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
]