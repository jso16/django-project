from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/register_email_newslatter/', views.register_email_newslatter, name='register_email_newslatter'),
]
