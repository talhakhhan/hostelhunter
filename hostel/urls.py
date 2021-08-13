from django.conf.urls import url
from . import views

app_name = 'hostel'

urlpatterns = [

    url(r'^hostels', views.hostels, name="hostels"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^about', views.about, name="about"),
    url(r'^boys_hostel', views.boys_hostel, name="boys_hostel"),
    url(r'^girls_hostel', views.girls_hostel, name="girls_hostel"),
    url(r'^signup', views.signup, name="signup"),
    # url(r'^login', views.loginUser, name="login"),
    # url(r'^logout', views.logoutUser, name="logout"),
    url(r'^user', views.userPage, name="userPage"),
]
