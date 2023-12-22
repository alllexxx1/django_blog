from django.contrib import admin
from django.contrib.admin import DateFieldListFilter, AllValuesFieldListFilter

from .models import Article, ArticleComment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),)


@admin.register(ArticleComment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    search_fields = ['id', 'content']
    list_filter = (('content', AllValuesFieldListFilter),)
