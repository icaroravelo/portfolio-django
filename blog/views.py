from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Create your views here.
def blogHomePage(request):
    posts = Post.objects.all() # Fetch all post data from database
    context = {
        "posts": posts,
    }
    return render(request, 'blog/main.html', context)

def blogCategory(request, tags):
    posts = Post.objects.filter(
        tags__name__contains=tags
    ).order_by("-created_at")
    context = {
        "tags": tags,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blogPost(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, pk=pk)
    context = {
        "post": post
    }
    return render(request, "blog/post.html", context)

def latestThreePosts(request, created_at):
    latests = Post.objects.filter(
        order_by = created_at
    )
    context = {
        "latests" : latests
    }
    return render(request, context)