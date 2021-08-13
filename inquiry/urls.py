from django.urls import path
from . import views
urlpatterns = [
    path('', views.inquiries, name="inquiries")
]
