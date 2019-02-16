from django.shortcuts import render, redirect
from .models import Feed, FeedComment, Like, Follow
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
class FeedListView(ListView):
    model = Feed  # 어떤 모델이 적용될 것인지
    template_name = 'feeds/index.html'  # default: feeds/feed_list.html
    # context variable이란 템플릿에서 쓰일 변수 이름과 파이썬 객체를 매핑한 딕셔너리 (rails partial view에서 locals에 전달되는 애)
    context_object_name = 'feeds'  # default: object_list, 모델을 다루는 경우 추가로 feed_list
    

# def index(request):
#     if request.method == 'GET':
#         feeds = Feed.objects.all()
#         return render(request, 'feeds/index.html', {'feeds': feeds})
#     elif request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         Feed.objects.create(title=title, content=content)
#         # POST 데이터 처리 후에는 언제나 HttpResponseRedirect를 반환해야 함
#         return redirect('/feeds')

class FeedCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/new.html'  # defalut: 'feeds/feed_create_form.html'.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

class FeedUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
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
    # template_name의 default: 'feeds/feed_confirm_delete.html'

# def delete(request, id):
#     feed = Feed.objects.get(id=id)
#     feed.delete()
#     return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    author = request.user # 추가
    FeedComment.objects.create(feed_id=id, content=content, author=author)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def feed_like(request, pk):
    feed = Feed.objects.get(id = pk)
    likeList = feed.like_set.filter(user_id = request.user.id)
    if likeList.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = pk)
    return redirect ('/feeds')

def Lets_Follow(request, pk):  # 모델 이름이랑 view 이름이 같으면 충돌남! (follow로 하면 안된다)
    follow_from = request.user
    follow_to = User.objects.get(id = pk)

    try:
        following_already = Follow.objects.get(follow_from=follow_from, follow_to=follow_to)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        # Follow.objects.create(follow_from=follow_from, follow_to=follow_to)
        f = Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()

    return redirect('/feeds')