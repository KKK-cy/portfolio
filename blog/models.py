from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(default='文章标题', max_length=60)
    date = models.DateField()
    img = models.ImageField(default='default.png', upload_to='images/')
    text = models.TextField(default='文章正文')

    def __str__(self):
        return self.title

    # 设置文章正文只显示前50个字
    def short_text(self):
        return self.text[:50]+'...'
