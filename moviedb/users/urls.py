from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/login', views.user_login, name='login'),
    url(r'^users/register', views.user_register, name='register'),
    url(r'^profile/(?P<pk>\d+)', views.UserProfileDetail.as_view(),
    name='profile_detail'),
    url(r'profile/(?P<pk>\d+)/update', views.UserProfileUpdate.as_view(),
        name='profile_edit')
]
