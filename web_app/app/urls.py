from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.IndexView.as_view()),
    url(r'^accounts/login', 'app.views.login_e', name='Unable login'),
]