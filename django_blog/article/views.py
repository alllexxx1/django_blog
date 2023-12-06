from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect


class ArticleView(View):

    def get(self, request, tags, article_id):
        response_text = f'Статья номер {article_id}. Тег {tags}'
        return HttpResponse(response_text)


# def index(request):
#     # url = reverse('article', args=['python', 42])
#     url = reverse('article', kwargs={'tags': 'PYTHON', 'article_id': 42})
#     return redirect(url)


class IndexView(View):
    def get(self, request):
        url = reverse('article', kwargs={'tags': 'PYTHON', 'article_id': 42})
        return HttpResponseRedirect(url)
