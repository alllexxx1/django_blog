from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Article.objects.bulk_create([Article(name='magic article', body='some info about MAGIC article'), Article(name='usual article', body='some info about USUAL article'),
#                              Article(name='unusual article', body='some info about UNUSUAL article'), Article(name='mega article', body='some info about MEGA article'),
#                              Article(name='tremendous article', body='some info about TREMENDOUS article')])
