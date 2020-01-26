from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name="posts_list"),
    path('', views.PostsView.as_view(), name="posts"),
]
