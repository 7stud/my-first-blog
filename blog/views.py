from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def list_of_posts(request):
    posts = (Post.objects
                 .filter(published_date__lte=timezone.now())
                 .order_by('published_date')
    )
    return render(request, 'blog/list_of_posts.html', {'posts': posts})
