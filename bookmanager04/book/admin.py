from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo

# 註冊書籍模型
admin.site.register(BookInfo)
# 註冊人物模型
admin.site.register(PeopleInfo)
