from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField('name', max_length=20)


class Tag(models.Model):
    name = models.CharField('name', max_length=16)


class Blog(models.Model):
    title = models.CharField('title', max_length=40)
    author = models.CharField('author', max_length=20)
    content = models.CharField('content', max_length=100000)
    created = models.DateTimeField('published time', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='category', on_delete=CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='tags')


class Comment(models.Model):
    name = models.CharField('name', max_length=20)
    email = models.CharField('email', max_length=20)
    content = models.CharField('content', max_length=200)
    created = models.DateTimeField('published time', auto_now_add=True)

    blog = models.ForeignKey(Blog, verbose_name='blog', on_delete=CASCADE)


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username
