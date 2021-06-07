from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name = 'index'),
    path('signup', views.signMeUp, name = 'signMeUp'),
    path('login', views.logMeIn, name = 'logMeIn'),
]