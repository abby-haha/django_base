from django.db import models

# Create your models here.
# 書籍列表信息模型
class BookInfo(models.Model):
    # id 系統已經自動定義好
    name = models.CharField(max_length=10)

    class Meta:
        db_table='bookinfo'
        verbose_name='書籍管理'

# 人物列表信息模型
class PeopleInfo(models.Model):
    name= models.CharField(max_length=10)
    gender=models.BooleanField()
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物管理'