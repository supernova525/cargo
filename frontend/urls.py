from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from frontend import views


urlpatterns = [
    url(r'dashboard/$', login_required(views.DashBoardView.as_view()), name='dashboard'),
    url(r'prealerts/$', login_required(views.PrealertView.as_view()), name='prealerts'),
    url(r'$', views.LandingView.as_view(), name='landing'),
]