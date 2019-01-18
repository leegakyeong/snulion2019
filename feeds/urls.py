from django.urls import path
from feeds import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]
