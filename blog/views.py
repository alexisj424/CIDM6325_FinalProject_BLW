from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.db.models import Q, Count
from .models import Post, Comment, Category, Tag
from .forms import PostForm, CommentForm


# ✅ Keep HTMX function
def _is_htmx(request):
    return request.headers.get("HX-Request") == "true"


# ✅ CLASS-BASED POST LIST
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.select_related("author", "category").prefetch_related("tags")
        q = self.request.GET.get("q", "").strip()
        category_slug = self.request.GET.get("category")
        tag_slug = self.request.GET.get("tag")

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(body__icontains=q))
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["q"] = self.request.GET.get("q", "").strip()
        context["categories"] = Category.objects.annotate(n=Count("posts")).order_by("name")
        context["tags"] = Tag.objects.annotate(n=Count("posts")).order_by("name")

        # ✅ HTMX partial
        if _is_htmx(self.request):
            return {
                "posts": context["posts"],
                "q": context["q"],
                "categories": context["categories"],
                "tags": context["tags"],
            }

        return context


# ✅ CLASS-BASED POST DETAIL
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(
            Post.objects.select_related("author", "category")
            .prefetch_related("tags", "comments"),
            pk=self.kwargs.get("pk")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                post=self.object,
                author=request.user,
                text=form.cleaned_data["text"]
            )
            return redirect("blog:post_detail", pk=self.object.pk)

        context = self.get_context_data(comment_form=form)
        return render(request, "blog/post_detail.html", context)


# ✅ CUSTOM MIXIN
class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or obj.author == self.request.user


# ✅ CREATE
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = "Post created successfully!"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        form.save_m2m()
        return redirect("blog:post_detail", pk=post.pk)


# ✅ UPDATE
class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = "Post updated successfully!"

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


# ✅ DELETE
class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")


