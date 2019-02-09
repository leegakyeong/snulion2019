# ./homes/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from faker import Faker
import datetime
import random


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=256)
    host = models.ForeignKey(User, on_delete=models.CASCADE)  # 추가
    address = models.TextField()
    # 예약 날짜는 특정하지 않고 숙소만 등록하고 싶은 경우를 위해 available_dates에 null=True 추가
    available_dates_start = models.DateField(default=datetime.date.today, null=True)
    available_dates_end = models.DateField(default=datetime.date.today() + datetime.timedelta(days=30), null=True) # 오늘로부터 30일 후
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            Home.objects.create(
                title=myfake.bs(),
                address=myfake.address(),
                available_dates_start=myfake.date(),
                available_dates_end=myfake.date()
            )

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 추가
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            home_id = random.randint(1, Home.objects.all().count())
            Review.objects.create(content=myfake.catch_phrase(), home=Home.objects.get(id=home_id))

    def __str__(self):
        return str(self.id)
