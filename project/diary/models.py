from django.db import models
from django.utils import timezone  #djangoではdatetime.nowの代わりにtimezone.nowで現在日時を取得する
# Create your models here.

class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.title
