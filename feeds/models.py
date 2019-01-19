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


class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE) # CASCADE는 삭제된 Feed를 참조하는 FeedComment들도 모두 삭제하라는 의미입니다.
    # ForeignKey는 디폴트로 id로 가져오게 되어있음.
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
