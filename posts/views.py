from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
import datetime
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-published')[:5]
    return render(request,'posts/index.html',
                  {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html',
                  {'post': post})

