
from django.contrib import admin
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'page', 'created_at')
    search_fields = ('body',)
    list_filter = ('created_at',)
