from django.shortcuts import render
from .models import Feed
from .models import Feed, FeedComment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class FeedListView(ListView): # ListView라는 애가 많은 변수와 메소드를 갖고 있음. 디폴트 값 중 필요한 것만 바꾸면 됨
    model = Feed  # 어떤 모델이 적용될 것인지
    template_name = 'feeds/index.html'  # default: feeds/feed_list.html
    context_object_name = 'feeds'  # default: object_list, 모델을 다루는 경우 추가로 feed_list

# # Create your views here.
# def index(request):
#     if request.method == 'GET': # index
#         feeds = Feed.objects.all()
#         return render(request, 'feeds/index.html', {'feeds': feeds})
#     elif request.method == 'POST': # create
#         title = request.POST['title']
#         content = request.POST['content']
#         Feed.objects.create(title=title, content=content)
#         return redirect('/feeds')

class FeedCreateView(CreateView):
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/new.html'  # defalut: 'feeds/feed_create_form.html'.

# def new(request):
#     return render(request, 'feeds/new.html', {})

class FeedDetailView(DetailView):
    model = Feed
    template_name = 'feeds/show.html'  # default: feeds/detail.html
    context_variable_name = 'feed'  # default: object

# def show(request, id):
#     if request.method == 'GET':
#         feed = Feed.objects.get(id=id)
#         return render(request, 'feeds/show.html', {'feed': feed})
#     elif request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         feed = Feed.objects.get(id=id)
#         feed.title = title
#         feed.content = content
#         feed.save()
#         feed.update_date()
#         return redirect('/feeds/' + str(id))

class FeedUpdateView(UpdateView):
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/edit.html'  # defalut: 'feeds/feed_update_form.html'.
    context_variable_name = 'feed'

# def edit(request, id):
#     feed = Feed.objects.get(id=id)
#     return render(request, 'feeds/edit.html', {'feed': feed})

class FeedDeleteView(DeleteView):
    model = Feed
    success_url = reverse_lazy('index')
    # template_name의 default값은 'feeds/feed_confirm_delete.html'

# def delete(request, id):    # delete라는 메소드가 이미 있으니까 사실 이 함수 만들 때는 'delete'라는 이름은 피해줘야 함
#     feed = Feed.objects.get(id=id)
#     feed.delete()
#     return redirect('/feeds')

def create_comment(request, id):    # id는 Feed id
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):   # 사실 id는 필요없고 cid만 있어도 됨. 모든 피드의 코멘트가 다 다른 id를 갖고 있기 때문에.
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')