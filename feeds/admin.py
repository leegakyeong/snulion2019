from django.contrib import admin
from .models import Feed, FeedComment

# Register your models here.
admin.site.register(Feed)
admin.site.register(FeedComment)
