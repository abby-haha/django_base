from django.db import models

# Create your models here.
# 書籍列表信息模型
class BookInfo(models.Model):
    # id 系統已經自動定義好
    name = models.CharField(max_length=10)

    class Meta:
        db_table='bookinfo'


    def __str__(self):
        return self.name

# 人物列表信息模型
class PeopleInfo(models.Model):
    name= models.CharField(max_length=10)
    gender=models.BooleanField()
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'


    def __str__(self):
        return self.name