from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show', kwargs={'pk': self.pk})

class EventComment(models.Model):
    content = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)