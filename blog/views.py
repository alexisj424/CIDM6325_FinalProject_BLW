# blog/views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by("-created_at")
    comment_form = CommentForm()
    return render(request, "blog/post_detail.html", {
        "post": post, "comments": comments, "comment_form": comment_form
    })

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created.")
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "title": "New Post"})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Simple role rule: only the author or staff can edit
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("blog:post_detail", pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "title": "Edit Post"})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("blog:post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        messages.success(request, "Comment added.")
    else:
        messages.error(request, "Could not add comment.")
    return redirect("blog:post_detail", pk=pk)
