from django.db import models
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField('記事名', max_length=100)
    published = models.DateTimeField('投稿日')
    image = models.ImageField('画像', upload_to='media/')
    body = models.TextField('本文')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) >= 100:
            ret = self.body[:100] + '...'
        else:
            ret = self.body
        return ret

    def after_days(self):
        return datetime.datetime.now().day - self.published.day


