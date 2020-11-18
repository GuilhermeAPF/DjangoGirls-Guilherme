from .models import Post
from django.utils import timezone
from .forms import PostForm, GenerateRandomPosts
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .tasks import create_random_posts


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete (request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def generate_random_posts(request):
    if request.method != 'POST':
        form = GenerateRandomPosts()
        return render (request, 'blog/create_random_posts.html', {'form': form})

    form = GenerateRandomPosts(request.POST)
    if form.is_valid():
        amount = form.cleaned_data.get('amount')
        create_random_posts(amount)
        return redirect ('post_list')
    return render(request, 'blog/create_random_posts.html', {'form': form})