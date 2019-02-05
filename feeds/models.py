from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # kwargs = keyword + arguments
        return reverse('show', kwargs={'pk': self.pk})  # CreateView, UpdateView의 default success_url

class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE) # foreignkey는 1:n에서 n이 가지고 있어야 한다. 무엇을 참조할 것이냐는 말이다. on_delete=models.CASCADE는 feed를 삭제하면 feedComments도 다 삭제해준다는 것(casecade = 작은 폭포)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
