from django.shortcuts import render
from .models import Feed

# Create your views here.
def index(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds/index.html', {'feeds': feeds})

def new(request):
    return render(request, 'feeds/new.html', {})
