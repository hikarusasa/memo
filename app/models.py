from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField('カテゴリ名',max_length=20)
    creatd_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name

class Description(models.Model):
    title = models.CharField('タイトル',max_length=30)
    text = models.TextField('本文')
    category = models.ForeignKey(
        Category,verbose_name='カテゴリ',on_delete=models.PROTECT,blank=True
    )
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return '[{0}] {1}'.format(self.category,self.title)
