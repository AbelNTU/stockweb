from django.conf.urls import url

from . import views

app_name = 'statistic'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='home'),

    ]
