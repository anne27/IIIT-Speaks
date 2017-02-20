from django.contrib import admin
from .models import Blog
from .forms import BlogForm

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ["Author", "BlogTitle", "Created", "Updated"]
	prepopulated_fields = {"BlogSlug": ("BlogTitle",),}
	form = BlogForm

admin.site.register(Blog, BlogAdmin)
