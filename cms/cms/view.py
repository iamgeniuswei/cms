from django.http import HttpResponse
from django.shortcuts import render
import os
import json
# 为了直接访问附件文件配置
from django.views.static import serve
from django.conf import settings
def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'hello.html', context)


def test_onlyoffice(request):
    return render(request, 'onlyoffice.html')

import requests

def upload(request):
    print("here")
    if request.method == 'POST':
        try:
            status = json.loads( request.body)
            code = status['status']
            if code == 2:
                url = status['url']
                f = requests.get(url)
                with open("1.docx", "wb") as code:
                    code.write(f.content)

        except Exception as e:
            print(str(e))

        result = {"error":0}
        return HttpResponse(json.dumps(result))