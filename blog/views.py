from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# Create your views here.


def home(request):
    context = {
        'title': 'Home Page',
         'posts':Post.objects.all()
         }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


def about(request):
    return render(request, 'blog/about.html')
