from django.http import HttpResponse
# from .models import Test
# from 
from model.models import Test, OfficeFile

def testdb(request):
    file = OfficeFile(name='url-to-example-document.docx',
                      last_key='Khirz6zTPdfd7',
     size=12345)
    file.save()
    return HttpResponse("<p>数据添加成功!</p>")

