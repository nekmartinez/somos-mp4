
from django.contrib import admin
from .models import Page
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'published_at', 'author')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('published_at',)
