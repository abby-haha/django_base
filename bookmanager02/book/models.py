from django.db import models

# Create your models here.
"""
1. 模型类 需要继承自 model.Model
2. 定义属性
    id 系统默认会生成
    属性名=model.类型（选项）
    
    2.1 属性名 对应 就是字段名
        不要使用 python,MySql关键字
        不要使用连续的下划线(__)
    2.2 类型 MySQL的类型
    2.3 选项 是否默认值
3. 改变表的名称
    默认表的名称是：子应用名_类名 都是小写
create table 'qq_user'(
    id int,
    name varchar(10) not null default;)
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    Is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字
        verbose_name = '书籍管理' 'admin站点使用的'


class PeopelInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOISE=(
        (1,'male'),
        (2,'female'),
    )

    name = models.CharField(max_length=10, unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOISE,default=1)
    description=models.CharField(max_length=100,null=True)
    Is_delete=models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加_id

    # 外键的级联操作
    # 主表 和 从表
    # 1 对 多
    # 书籍 对 任务

    # 主表的一条数据 如果删除了
    # 从表有关联的数据， 关联的数据怎么办了呢
    # SET_NULL
    # 抛出异常，不让删除 PROTECT
    # 级联删除 CASCADE

    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'
        verbose_name='人物管理'