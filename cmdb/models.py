from django.db import models

# Create your models here.
class bookInfo(models.Model):
    ranking = models.CharField(max_length=3, primary_key=True, default="")
    bookname=models.CharField(max_length=32,default="")
    infos=models.CharField(max_length=50,default="")
    appraise = models.CharField(max_length=32, default="")
    peoplenum=models.CharField(max_length=32, default="")
    content= models.CharField(max_length=100, default="")