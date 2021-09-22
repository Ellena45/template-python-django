from django.shortcuts import render
from .models import BlogPost


def index(request):
    return render(request,'blog/base.html')

def timeline_view(request):
    posts = BlogPost.objects.filter(user=request.user)
    return render(request,'blog/timeline.html', {'posts':posts})