from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from .models import Blog, Comment
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from django import forms
from django.contrib.auth.models import User


def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def loginview(request):
    return render(request, 'login.html')


def login_view(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/blogs/')
                response.set_cookie('username', username, 3600)
                return response
            else:

                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf},)


def index(request):
    username = request.COOKIES.get('cookie_username', '')
    return render_to_response('index.html', {'username': username})


def logout(request):
    response = HttpResponse('logout!<br><a href="127.0.0.1:8000/regist>regist</a>"')
    response.delete_cookie('cookie_username')
    return render_to_response('logout.html')


@csrf_protect
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            registAdd = User.objects.create(username=username, password=password)
            #return render_to_response('regist.html', {'registAdd': registAdd, 'username': username})
            return render_to_response('regist.html', context_instance=RequestContext(request))

    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf})
