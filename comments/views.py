from django.shortcuts import render

# Create your views here.
from comments.models import Post, Comment


def main(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    lst = {
        'posts': posts,
        'comments': comments
    }
    return render(request, 'main.html', context=lst)