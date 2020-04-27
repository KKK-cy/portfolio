# Generated by Django 3.0.3 on 2020-04-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='img',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=30),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='在这里写作品的简介', max_length=100),
        ),
    ]
