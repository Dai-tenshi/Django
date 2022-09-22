from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def two(request):
    return render(request, 'main/two.html')
