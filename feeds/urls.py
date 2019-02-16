from django.urls import path
from feeds import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.FeedListView.as_view(), name='index'),

    # path('new/', views.new, name='new'),
    path('new/', views.FeedCreateView.as_view(), name='new'),

    # path('<int:id>/', views.show, name='show'),
    path('<int:pk>/', views.FeedDetailView.as_view(), name='show'),

    # path('<int:id>/edit', views.edit, name='edit'),
    path('<int:pk>/edit', views.FeedUpdateView.as_view(), name='edit'),

    # path('<int:id>/delete', views.delete, name='delete'),
    path('<int:pk>/delete', views.FeedDeleteView.as_view(), name='delete'),

    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/like/', views.feed_like, name='like'),
]
