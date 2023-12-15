from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, ArticleComment
from .forms import ArticleCommentForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={'article': article}
        )


class ArticleCommentFormView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()
        return render(request, 'articles/comment_form.html', {'form': form})

    def post(self, requset, *args, **kwargs):
        form = ArticleCommentForm(requset.POST)
        if form.is_valid():
            form.save()

        return redirect('articles_index')


class ArticleCommentView(View):

    def get(self, request, *args, **kwargs):
        comments = ArticleComment.objects.all()
        return render(
            request,
            'articles/comments.html',
            {'comments': comments}
        )
