from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'hello.html', context)


def test_onlyoffice(request):
    return render(request, 'onlyoffice.html')