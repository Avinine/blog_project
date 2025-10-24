from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all() # همه ی پست هارو از دیتابیس میگیره
    return render(request, 'blog/home.html', {'post': posts})
