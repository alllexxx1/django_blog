from django.contrib import admin
from django.contrib.admin import AllValuesFieldListFilter

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ['name']
    list_filter = (('name', AllValuesFieldListFilter),)
