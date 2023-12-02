from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def about(request):
    return render(request, 'about.html')


def about1(request):
    tags = ['m', 'mm', 'mmm', '111']
    return render(
        request,
        'about1.html',
        context={'tags': tags},
    )