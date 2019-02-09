# ./homes/urls.py
from django.conf.urls import include
from django.urls import path
from homes import views

app_name = 'homes' # 추가
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
]