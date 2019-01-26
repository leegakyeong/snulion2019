from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class FeedListView(ListView):
    model = Feed  # 어떤 모델이 적용될 것인지
    template_name = 'feeds/index.html'  # default: feeds/feed_list.html
    context_object_name = 'feeds'  # default: object_list, 모델을 다루는 경우 추가로 feed_list
    # -> 함수형 뷰 render 안에서 중괄호로 전달하는 것

class FeedDetailView(DetailView):
    model = Feed
    template_name = 'feeds/show.html'  # default: feeds/detail.html
    context_variable_name = 'feed'  # default: object

class FeedCreateView(CreateView):
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/new.html'  # defalut: 'feeds/feed_create_form.html'.

class FeedUpdateView(UpdateView):
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/edit.html'  # defalut: 'feeds/feed_update_form.html'.
    context_variable_name = 'feed'

class FeedDeleteView(DeleteView):
    model = Feed
    success_url = reverse_lazy('index') # 삭제하면 그거의 show 페이지로 갈 수 없으니까 다른 페이지로 가라고 하는 것!
    # template_name의 default값은 'feeds/feed_confirm_delete.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
# Create your views here.
# def index(request):
#     if request.method == 'GET': # index
#         feeds = Feed.objects.all()
#         return render(request, 'feeds/index.html', {'feeds': feeds})
#     elif request.method == 'POST': # create
#         title = request.POST['title']
#         content = request.POST['content']
#         Feed.objects.create(title=title, content=content)
#         return redirect('/feeds')

# def new(request):
#     return render(request, 'feeds/new.html', {})

# def show(request, id):
#     if request.method == 'GET': # show
#         feed = Feed.objects.get(id=id)
#         return render(request, 'feeds/show.html', {'feed': feed})
#     elif request.method == 'POST': # update
#         title = request.POST['title']
#         content = request.POST['content']
#         feed = Feed.objects.get(id=id)
#         feed.title = title
#         feed.content = content
#         feed.save()
#         feed.update_date()
#         return redirect('/feeds/' + str(id))

# def edit(request, id):
#     feed = Feed.objects.get(id=id)
#     return render(request, 'feeds/edit.html', {'feed': feed})
#
# def delete(request, id):
#     feed = Feed.objects.get(id=id)
#     feed.delete()
#     return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')
