from django.db import models
from django.utils import timezone

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show', kwargs={'pk': self.pk}) # 여기로 리다이렉트해라..>?
        # CreateView, UpdateView의 default success_url
        # url의 이름을 view에서 어떻게 사용하느냐
        # **? kwargs란: 딕셔너리 형태로 되어 있어서 두 번 풀어 줘야 함

class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
