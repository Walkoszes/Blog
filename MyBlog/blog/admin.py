from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    list_filter = ("published_date", "content")
    search_fields = ("title", "content")