from django.shortcuts import render
from .models import Event, EventComment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class EventListView(ListView):
    model = Event  # 어떤 모델이 적용될 것인지
    template_name = 'events/index.html'  # default: events/event_list.html
    context_object_name = 'events'  # default: object_list, 모델을 다루는 경우 추가로 feed_list

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/show.html'  # default: events/detail.html
    context_variable_name = 'event'

class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'date']
    template_name = 'events/new.html'

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'date']
    template_name = 'events/edit.html'
    context_variable_name = 'event'

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('index')

def create_comment(request, id):
    content = request.POST['content']
    EventComment.objects.create(event_id=id, content=content)
    return redirect('/events')

def delete_comment(request, id, cid):
    c = EventComment.objects.get(id=cid)
    c.delete()
    return redirect('/events')