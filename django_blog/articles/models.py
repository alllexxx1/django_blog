from django.db import models
from django_blog.categories.models import Category


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    content = models.CharField('content', max_length=100)
