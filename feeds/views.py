from django.shortcuts import render, redirect
from .models import Feed, FeedComment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin



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
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
