# ./homes/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Home, Review
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request):
    if request.method == 'GET': # index
        homes = Home.objects.all()
        return render(request, 'homes/index.html', {'homes': homes})
    elif request.method == 'POST': # create
        title = request.POST['title']
        address = request.POST['address']
        available_dates_start = request.POST['available_dates_start']
        available_dates_end = request.POST['available_dates_end']
        if available_dates_start == "": # ""는 date가 아니므로
            available_dates_start = None
        if available_dates_end == "":
            available_dates_end = None
        Home.objects.create(
            title=title,
            address=address,
            available_dates_start=available_dates_start,
            available_dates_end=available_dates_end
        )
        return redirect('/homes')


def new(request):
    return render(request, 'homes/new.html', {})


def show(request, id):
    if request.method == 'GET': # show
        home = get_object_or_404(Home, pk=id) # 해당 id의 object가 없을 경우 404 에러를 띄워 줌. 편리!
        return render(request, 'homes/show.html', {'home': home})
    elif request.method == 'POST': # update
        title = request.POST['title']
        address = request.POST['address']
        available_dates_start = request.POST['available_dates_start']
        available_dates_end = request.POST['available_dates_end']
        if available_dates_start == "":
            available_dates_start = None
        if available_dates_end == "":
            available_dates_end = None
        home = Home.objects.get(id=id)
        home.title = title
        home.address = address
        home.available_dates_start = available_dates_start
        home.available_dates_end = available_dates_end
        home.save()
        home.update_date()
        return redirect('/homes/' + str(id))


def edit(request, id):
    home = Home.objects.get(id=id)
    return render(request, 'homes/edit.html', {'home': home})


def delete(request, id):
    home = Home.objects.get(id=id)
    home.delete()
    return redirect('/homes')


def create_review(request, id):
    content = request.POST['content']
    Review.objects.create(home_id=id, content=content)
    return redirect('/homes')


def delete_review(request, id, review_id):
    c = Review.objects.get(id=review_id)
    c.delete()
    return redirect('/homes')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
