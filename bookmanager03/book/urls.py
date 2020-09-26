from django.urls import path

from book.views import index, shop,register,req_json,method,redirect_url
from book.views import set_cookies,get_cookies,response,response_json
from book.views import set_get_cookies,set_session,get_session,del_session


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
    path('req_json/',req_json),
    path('method/',method),
    path('set_cookies/',set_cookies),
    path('get_cookies/',get_cookies),
    path('res/',response),
    path('res_json/',response_json),
    path('redirect_url/',redirect_url),
    path('set_get_cookies/',set_get_cookies),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('del_session/',del_session),

]
