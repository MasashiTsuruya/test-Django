from django.db import models
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    name       = models.CharField('部署名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name

class Club(models.Model):
    name       = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name  = models.CharField('姓', max_length=20)
    email      = models.EmailField('メールアドレス', blank=True)     #blanl=Trueで必須ではない項目にする。
    depatment  = models.ForeignKey(           #on_delete=models.PROTECTで既に紐づいているものは削除できなくする。
        Department, verbose_name='部署', on_delete=models.PROTECT,
    )
    club       = models.ManyToManyField(Club, verbose_name='部活')
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{0}{1}{2}'.format(self.first_name, self.last_name, self.depatment)
