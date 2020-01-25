from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostsListView(ListView):
    context_object_name = "posts"
    model = Post
    paginate_by = 3
    template_name = 'lists_of_posts.html'
