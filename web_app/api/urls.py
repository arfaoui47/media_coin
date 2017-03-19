from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userData', views.UserData.as_view()),
]