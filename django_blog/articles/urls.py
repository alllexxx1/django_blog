from django.urls import path
from .views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/', ArticleView.as_view(), name='articles_detail'),
]
