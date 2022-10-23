
from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    path('name/', views.name, name="name"),
    path('result/', views.result, name="result"),
    ]
