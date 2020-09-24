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
book.save()  # 必须调用对象的方法 save()将数据保存到数据库

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

############################## 删除数据 ############################
# 删除分2种，物理删除（这条记录的数据 删除） 和 逻辑删除 （修改标记位 例如 is_delete=False)

# 方法1:
book=BookInfo.objects.get(id=6)
book.delete()

# 方式2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()


# ##################### 查询 #################################
# get 查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
try:
    book=BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all 查询多个结果
BookInfo.objects.all()
from book.models import PeopelInfo
PeopelInfo.objects.all()

# count 查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

############################# 过滤查询 #################################
# 实现SQL中的where功能，包括

# filter 过滤出多个结果
# exclude 排除掉符合条件剩下的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值) 获取n个结果 n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值) 获取n个结果 n=0,1,2,...
# 模型类名.objects.get(属性名__运算符=值) 获取1个结果 或者异常

# 查询编号为1的图书
book=BookInfo.objects.get(id=1) #简写形式（属性名=值）
book=BookInfo.objects.get(id__exact=1) #完整形式
BookInfo.objects.get(pk=1) #pk primary key 主键
BookInfo.objects.exclude(id=1)  # 查询除了id=1的其他书
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(name__isnull=False) # 书名不为空

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
BookInfo.objects.filter(id__gte=3) #大于等于3

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
BookInfo.objects.filter(pub_date__month=5) # 5月

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')