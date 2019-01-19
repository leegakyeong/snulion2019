from django.urls import path
from feeds import views

urlpatterns = [
    path('', views.index, name='index'), # name은 url을 변수로 쓰기 위해서 지정해주는 것
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
]
