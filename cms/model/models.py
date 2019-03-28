from django.db import models

# Create your models here.
# models.py
# from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)


class OfficeFile(models.Model):
    name = models.CharField(max_length=256)
    size = models.IntegerField()
    last_key = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True, auto_created=True)
    update_time = models.DateTimeField(auto_now=True, auto_created=True)