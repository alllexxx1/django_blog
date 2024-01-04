from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Article, ArticleComment
from .forms import ArticleForm, ArticleCommentForm


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


class ArticleCommentView(View):

    def get(self, request, *args, **kwargs):
        comments = ArticleComment.objects.all()[5:]
        return render(
            request,
            'articles/comments.html',
            {'comments': comments}
        )


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/article_create.html', {'form': form})

    def post(self, requset, *args, **kwargs):
        form = ArticleForm(requset.POST)
        if form.is_valid():
            form.save()
            messages.success(requset, "Your action was successful! Congrats!")
            return redirect('articles_index')
        return render(requset, 'articles/article_create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/article_edit.html',
                      {'form': form, 'article_id': article_id})

    def post(self, requset, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        previous_article_title = article.name
        form = ArticleForm(requset.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(requset, f'You have updated the {previous_article_title} article!')
            return redirect('articles_index')
        return render(requset, 'articles/article_edit.html',
                      {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, f'The article {article.name} has been deleted')
        return redirect('articles_index')


class ArticleCommentFormView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()
        return render(request, 'articles/comment_form.html', {'form': form})

    def post(self, requset, *args, **kwargs):
        form = ArticleCommentForm(requset.POST)
        if form.is_valid():
            form.save()
            messages.success(requset, 'Your comment has been added successfully!')
        return redirect('comments_index')
