from django.urls import path
from django_blog.articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
    path('comment/', views.ArticleCommentFormView.as_view(), name='comment_create'),
    path('comments/', views.ArticleCommentView.as_view(), name='comments_index')
]
