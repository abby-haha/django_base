from django.http import HttpResponse

# Create your views here.
from book.models import BookInfo


def index(resquest):
    #  在这里实现 增删改查
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("index")


# ############################增加数据##############################
# 方式1
book = BookInfo(
    name='Django',
    pub_date='2020-1-1',
    readcount=100,
)
book.save()  # 调用models 中的方法 save()将数据保存到数据库

# 方式2
# object -- 相当于一个代理 实现增删改查
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100
)

# ############################修改数据##############################
# 方法1 select * from bookinfo where id =6;
book = BookInfo.objects.get(id=6)
book.name = '运维入门方法'
book.commentcount = 666
book.save()

# 方法2 select * from bookinfo where id =6;
BookInfo.objects.filter(id=5).update(name='python入门方法', commentcount=999)


# ##################### 查询 #################################
# get 查询单一结果，如果不存在会抛出