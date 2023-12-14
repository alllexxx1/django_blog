from django.db import models
from django_blog.categories.models import Category


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Article.objects.bulk_create([Article(name='usual articles', body='some info about USUAL articles', category='good'), Article(name='unusual articles', body='some info about UNUSUAL articles', category='good'),
#                             Article(name='mega articles', body='some info about MEGA articles', category='splendid'), Article(name='tremendous articles', body='some info about TREMENDOUS articles', category='splendid')])

