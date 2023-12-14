from django.urls import path
from .views import IndexView, CategoryView


urlpatterns = [
    path('', IndexView.as_view(), name='categories_index'),
    path('<int:id>/', CategoryView.as_view(), name='categories_detail')
]
