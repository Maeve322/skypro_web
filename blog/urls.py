from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogPostListView.as_view(), name="blogpost_list"),
    path(
        "blog/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"
    ),
    path("create/", BlogPostCreateView.as_view(), name="blogpost_form"),
    path(
        "blog/<int:pk>/update/",
        BlogPostUpdateView.as_view(),
        name="blogpost_update",
    ),
    path(
        "blog/<int:pk>/delete/",
        BlogPostDeleteView.as_view(),
        name="blogpost_delete",
    ),
]
