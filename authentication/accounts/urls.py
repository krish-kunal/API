from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path("login",views.login,name='login page'),
    path("create",views.create,name='new account'),
    path("forgot",views.reset,name='change password'),
    path("reset",views.reset,name='reset password'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)