from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feeds/new.html', {})

def show(request, id):
    if request.method == 'GET': #show
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/show.html', {'feed': feed})
    elif request.method == 'POST': # update
        title = request.POST['title']
        content = request.POST['content']
        feed = Feed.objects.get(id=id)
        feed.title = title
        feed.content = content
        feed.save()
        feed.update_date()
        return redirect('/feeds/' + str(id))

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feeds/edit.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')
