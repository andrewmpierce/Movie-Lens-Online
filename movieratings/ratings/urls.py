from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^top_20.html$', views.top_twenty, name='top_twenty'),
    url(r'^movies/(?P<movie_id>\d+)$', views.show_movies, name='show_movies')

]
