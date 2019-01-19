from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def show(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/show.html', {'feed' : feed})
    elif request.method == 'POST':  # update
        title = request.POST['title']
        content = request.POST['content']
        feed = Feed.objects.get(id=id)
        feed.title = title
        feed.content = content
        feed.save()
        feed.update_date()
        return redirect('/feeds/' + str(id))

def new(request):
    return render(request, 'feeds/new.html', {})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feeds/edit.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')