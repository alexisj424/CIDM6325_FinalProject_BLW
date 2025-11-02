# blog/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.order_by("-created_at")

    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to comment.")
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                text=form.cleaned_data["text"],
            )
            messages.success(request, "Comment posted.")
            return redirect("blog:post_detail", pk=post.pk)
        else:
            messages.error(request, "Please fix the errors in your comment.")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": form},
    )


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, "Post created.")
            return redirect("blog:post_detail", pk=obj.pk)
        messages.error(request, "Please fix the errors below.")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, "You don’t have permission to edit this post.")
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("blog:post_detail", pk=pk)
        messages.error(request, "Please fix the errors below.")
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form, "post": post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, "You don’t have permission to delete this post.")
        return redirect("blog:post_detail", pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {"post": post})
