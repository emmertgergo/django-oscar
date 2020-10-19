from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def bootstrap_test(request):
    return render(request, 'bootstrap_test.html')
