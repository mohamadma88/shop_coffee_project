from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('auth', 'title', 'pub', 'created_at')
    list_filter = ('auth','pub','created_at')
    search_fields = ['auth','title']
