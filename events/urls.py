from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='index'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='show'), # pk = primary key
    path('new/', views.EventCreateView.as_view(), name='new'),
    path('<int:pk>/edit', views.EventUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name='delete'),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
]
