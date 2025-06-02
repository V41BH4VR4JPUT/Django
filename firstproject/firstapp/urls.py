from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello),
    path('class', views.HelloView.as_view()),
    path('reservation', views.Home),
]