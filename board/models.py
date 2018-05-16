from django.db import models
from user_auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField('内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日時', auto_now_add=True)


class Board(models.Model):
    title = models.CharField('タイトル', max_length=50)
    body = models.TextField('内容')
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment, verbose_name='コメント')
    created_at = models.DateTimeField('投稿日時', auto_now_add=True)
    updated_at = models.DateTimeField('変更日時', auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) < 100:
            return self.body
        else:
            return self.body[:100] + '...'
