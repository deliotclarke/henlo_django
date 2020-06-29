from django.urls import path
from henlo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("henlo/<name>", views.henlo_there, name="henlo_there")
]