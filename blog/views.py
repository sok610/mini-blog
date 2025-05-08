from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type') # 'title' or 'content'

    if query:
        if search_type == 'title':
            posts = Post.objects.filter(title__icontains=query)
        else:
            posts = Post.objects.filter(content__icontains=query)
        posts = posts.order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(author=request.user, title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_create.html')

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect('post_list')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('post_list')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'blog/signup.html', {'error': 'Username already taken'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('post_list')
    return render(request, 'blog/signup.html')

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        messages.success(request, "Post updated successfully.")
        return redirect('my_posts')
    
    return render(request, 'blog/post_edit.html', {'post': post})
