from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "content",
        "preview",
        "created_at",
        "is_published",
        "view_count",
    )
    list_filter = ("title",)
    search_fields = ("title", "is_published")
