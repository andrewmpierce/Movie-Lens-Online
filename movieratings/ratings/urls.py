from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^top_20.html$', views.top_twenty, name='top_twenty'),
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'users/(?P<rater_id>\d+)$', views.rater_detail, name='rater_detail'),
    url(r'$', views.top_20, name='top_20')
    ]
