# ./homes/models.py
from django.db import models
from django.utils import timezone 
import datetime


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    # 예약 날짜는 특정하지 않고 숙소만 등록하고 싶은 경우를 위해 available_dates에 null=True 추가
    available_dates_start = models.DateField(default=datetime.date.today, null=True)
    available_dates_end = models.DateField(default=datetime.date.today() + datetime.timedelta(days=30), null=True) # 오늘로부터 30일 후
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title



