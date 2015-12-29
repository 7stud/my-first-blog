from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def list_of_posts(request):
    return render(request, 'blog/list_of_posts.html', {})
