from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),

    #/mssic/album_id
    url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail1'),

    # ex: /polls/5/results/
    url(r'^[0-9]+/results_(?P<question_id>[0-9])/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^[0-9]+/vote_(?P<question_id>[0-9]+)/$', views.vote, name='vote'),
]
