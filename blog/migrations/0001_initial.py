# Generated by Django 3.0.3 on 2020-04-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='文章标题', max_length=60)),
                ('date', models.DateField()),
                ('img', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='文章正文')),
            ],
        ),
    ]
