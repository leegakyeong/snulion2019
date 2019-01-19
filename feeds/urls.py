from django.urls import path
from feeds import views

urlpatterns = [
    # .as_view()는 아직 클래스의 인스턴스가 없어서, 자동으로 인스턴스를 만들어주는 거다.
    # queryset은 구체적이고 명확하게 말해줄 때. model = Feed는 queryset으로 풀어쓰면 queryset = Feed.objects.all
    path('', views.FeedListView.as_view(), name='index'), # name은 url을 변수로 쓰기 위해서 지정해주는 것
    path('new/', views.FeedCreateView.as_view(), name='new'),
    path('<int:pk>/', views.FeedDetailView.as_view(), name='show'), #pk는 primary key
    path('<int:pk>/edit', views.FeedUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.FeedDeleteView.as_view(), name='delete'),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
]
