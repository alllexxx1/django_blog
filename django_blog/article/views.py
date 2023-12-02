from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'article/index.html',
        context={'app_name': 'article'}
    )
