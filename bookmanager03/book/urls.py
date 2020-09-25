from django.urls import path

from book.views import index, shop,register,json,method
from book.views import set_cookies,get_cookies


############################## 自定义路由转换器 ######################
from django.urls import converters
from django.urls.converters import register_converter
# 自定义路由转换器
class Mobile:
    # 判断路由是否符合正则，符合则返回给python的视图
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     return str(value)

# 注册mobile转换器
# register_converter(转换器类,'转换器名字')
register_converter(Mobile,'phone')

urlpatterns = [

    path('index/',index),
    path('<int:aa>/<phone:bb>/',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('set_cookies/',set_cookies),
    path('get_cookies/',get_cookies),

]