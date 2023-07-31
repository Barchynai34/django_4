from django.contrib import admin
from posts.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status", "category"]
    list_filter = ["status", "category"]
    list_editable = ["status"]