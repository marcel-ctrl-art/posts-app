from django.core.paginator import Paginator  # for vanilla View
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post


class PostsListView(ListView):
    context_object_name = "posts"
    model = Post
    ordering = ["-created_at"]
    paginate_by = 3
    template_name = "lists_of_posts.html"


class PostsView(View):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        paginator = Paginator(posts, 3)
        page = request.GET.get("page")
        posts = paginator.get_page(page)

        ctx = {
            "posts": posts,
        }

        return render(request, "posts_view.html", ctx)


def post_view_foo(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by("-created_at")
        paginator = Paginator(posts, 3)
        page = request.GET.get("page")
        posts = paginator.get_page(page)

        ctx = {
            "posts": posts
        }

        return render(request, "post_view_foo.html", ctx)
