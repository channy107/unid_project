from django.db import models



class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    description=models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
