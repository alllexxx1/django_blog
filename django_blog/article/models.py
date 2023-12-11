from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Article.objects.bulk_create([Article(name='magic articles', body='some info about MAGIC articles'), Article(name='usual articles', body='some info about USUAL articles'),
#                              Article(name='unusual articles', body='some info about UNUSUAL articles'), Article(name='mega articles', body='some info about MEGA articles'),
#                              Article(name='tremendous articles', body='some info about TREMENDOUS articles')])
