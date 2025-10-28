from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, created_at=timezone.now())
    return redirect(request, 'blog/post_new.html')

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
