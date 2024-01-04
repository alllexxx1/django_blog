from django.urls import path
from django_blog.articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('create/', views.ArticleFormCreateView.as_view(), name='article_create'),
    path('<int:id>/update/', views.ArticleFormEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
    path('create_comment/', views.ArticleCommentFormView.as_view(), name='comment_create'),
    path('comments/', views.ArticleCommentView.as_view(), name='comments_index')
]
