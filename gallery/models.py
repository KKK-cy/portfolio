from django.db import models

# Create your models here.
""" 创建app要实现的功能 """

class Gallery(models.Model):
    description = models.CharField(max_length=100)


