from django.urls import path, re_path
from . import views

urlpatterns = [
    path('profile/', views.profile), 
    re_path(r'^profile/$', views.profile), 
]
