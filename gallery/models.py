from django.db import models

# Create your models here.
""" 创建app要实现的功能 """

class Gallery(models.Model):
    # 作品描述
    description = models.CharField(default="在这里写作品的简介",max_length=100)
    # 作品图片(可以指定默认图片为default.png，这样创建gallery没有上传图片时会有默认图片;还可以指定图片的上传路径)
    img = models.ImageField(default='default.png',upload_to='images/')
    # 作品标题
    title = models.CharField(default='作品标题',max_length=30)

    # admin管理后台就会显示作品的标题
    def __str__(self):
        return self.title
