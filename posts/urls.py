from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.PostsView.as_view(), name="posts_class"),
    path('foo/', views.post_view_foo, name="posts_foo"),
    path('generic/', views.PostsListView.as_view(), name="posts_generic"),

]
