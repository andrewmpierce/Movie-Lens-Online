from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^top', views.top_movies, name='top_twenty'),
    url(r'^movies/(?P<movie_id>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'^users/(?P<rater_id>\d+)$', views.rater_detail, name='rater_detail')
]
