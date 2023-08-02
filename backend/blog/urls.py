from django.urls import path

from .views import BlogListView, DetailPostView

app_name='blog'

urlpatterns = [
    path('posts/', BlogListView.as_view()),
    path('posts/<post_slug>', DetailPostView.as_view()),
]