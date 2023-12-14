from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Category


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(
            request,
            'categories/index.html',
            context={'categories': categories}
        )


class CategoryView(View):

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        return render(
            request,
            'categories/category.html',
            context={'category': category}
        )
