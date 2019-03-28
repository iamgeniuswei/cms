from django.http import HttpResponse
from django.shortcuts import render
import os
import json
# 为了直接访问附件文件配置
from django.views.static import serve
from django.conf import settings

# 访问数据库中所有待编辑的文件
from model.models import OfficeFile


def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'hello.html', context)

def test_file_list(request):
    origin = OfficeFile.objects.all()
    list = []
    for item in origin:
        list.append(item)
    return render(request, 'list.html', {'list':list})



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
                path = os.path.join(settings.MEDIA_ROOT, "url-to-example-document.docx")
                with open(path, "wb") as code:
                    code.write(f.content)

        except Exception as e:
            print(str(e))

        result = {"error":0}
        return HttpResponse(json.dumps(result))