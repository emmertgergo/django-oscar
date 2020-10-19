from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def bootstrap_test(request):
    return render(request, 'bootstrap_test.html')


def bootstrap_row_columns(request):
    return render(request, 'bootstrap_row_columns.html')