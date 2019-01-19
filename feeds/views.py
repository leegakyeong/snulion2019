from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect

# Create your views here.
'''
def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')
'''

from django.views.generic import ListView, DetailView

class FeedListView(ListView):
    model = Feed  # 어떤 모델이 적용될 것인지
    # queryset = Feed.objects.all()
    template_name = 'feeds/index.html'  # default: feeds/feed_list.html
    context_object_name = 'feeds'  # default: object_list, 모델을 다루는 경우 추가로 feed_list

class FeedDetailView(DetailView):
    model = Feed
    template_name = 'feeds/show.html'  # default: feeds/detail.html
    context_variable_name = 'feed'  # default: object

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class FeedCreateView(CreateView): # new 함수 대신에 만들어줌
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/new.html'  # defalut: 'feeds/feed_create_form.html'.

class FeedUpdateView(UpdateView): # edit 함수 대신에 만들어줌
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/edit.html'  # default: 'feeds/feed_update_form.html'.
    context_variable_name = 'feed'

class FeedDeleteView(DeleteView): # delete 함수 대신에 만들어줌
    model = Feed
    success_url = reverse_lazy('index') # success 했을 때 어디로 갈지 알려주는 애가 바로 success_url
    # reverse_lazy()는 reverse()와 같으나 좀 기다렸다가 reverse하는 것!
    # template_name의 default값은 'feeds/feed_confirm_delete.html'


'''
def show(request, id):
    if request.method=='GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/show.html', {'feed': feed})
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
'''

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')