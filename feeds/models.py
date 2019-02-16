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
    like_user_set = models.ManyToManyField(User, blank=True, related_name='user_like_set', through='Like')
    # User에서 접근할 때 related_name으로 feed에 접근할 수 있다.

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

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Follow(models.Model): # 얘를 추가해주세요!
    follow_to = models.ForeignKey(User, related_name = 'follow_from', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(User, related_name = 'follow_to', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('follow_to', 'follow_from')

    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)

User.add_to_class('follows', models.ManyToManyField('self', through = Follow, related_name = 'follow', symmetrical=False))
# symmetrical은 default가 true임. 강제 맞팔.