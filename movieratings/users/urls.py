from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/reg', views.user_register, name='user_register'),
    url(r'^users/login', views.user_login, name='user_login')

    ]
