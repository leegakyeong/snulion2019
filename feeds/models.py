from django.db import models
from django.utils import timezone # django는 created_at과 updated_at을 알아서 만들어주지 않음
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    # id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def update_date(self): # 나중에 수정할 때 씀
        self.updated_at = timezone.now()
        self.save

    def __str__(self):
        return self.title  # 콘솔에서 모델 가져와라 하면 다 보여주는 게 아니라 제목만 보여주게 됨

    def get_absolute_url(self):
        return reverse('show', kwargs={'pk': self.pk})  # CreateView, UpdateView의 default success_url

class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)