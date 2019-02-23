from django.shortcuts import render
from .models import Feed, FeedComment, Like, Follow
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.middleware import csrf



class FeedListView(ListView):
    #model = Feed #어떤 모델이 적용될지
    queryset = Feed.objects.order_by('-created_at')
    template_name = 'feeds/index.html' # default: feeds/feed_list.html
    context_object_name = 'feeds' #default: object_list, 모델을 다루는 경우는 추가로 feed_list

class FeedDetailView(DetailView):
    model = Feed
    template_name = 'feeds/show.html'
    context_variable_name = 'feed'

class FeedCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/new.html'  # defalut: 'feeds/feed_create_form.html'.
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class FeedUpdateView(UpdateView):
    model = Feed
    fields = ['title', 'content']
    template_name = 'feeds/edit.html'  # defalut: 'feeds/feed_update_form.html'.
    context_variable_name = 'feed'

class FeedDeleteView(DeleteView):
    model = Feed
    success_url = reverse_lazy('index')
    # template_name의 default값은 'feeds/feed_confirm_delete.html'

def feed_like(request, pk):
    feed = Feed.objects.get(id = pk)
    likeList = feed.like_set.filter(user_id = request.user.id)
    if likeList.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = pk)
    return redirect ('/feeds')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feeds/new.html', {})

def show(request, id):
    if request.method == 'GET': # show
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

def create_comment(request, id):
    if request.method == 'POST':
        content = request.POST.get('content')
        author = User.objects.get(id=request.user.id)
        response_data = {}

        token = request.META.get('CSRF_COOKIE', None)
        if token is None:
            token = csrf._get_new_csrf_key()
            request.META['CSRF_COOKIE'] = token
        request.META['CSRF_COOKIE_USED'] = True

        comment = FeedComment.objects.create(feed_id=id, content=content, author=author)
        response_data['content'] = comment.content
        response_data['comment_id'] = comment.id
        response_data['feed_id'] = comment.feed_id
        response_data['comment_author'] = comment.author.username
        response_data['token'] = token

    return JsonResponse(response_data)

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

def Lets_Follow(request, pk): #추가
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