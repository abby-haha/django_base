from MySQLdb.constants.FIELD_TYPE import JSON
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
def weather(request, city, year):
    return HttpResponse('weather')


# 查询字符串（query string)，形如key1=value1&key2=value2；
def login(request):
    response = request.GET.get('name')
    # 相当于（但如果name不存在，则报错)：response = request.GET['name']
    print(response)
    # abby

    return HttpResponse('login')


# 请求体（body）中发送的数据，比如表单数据、json、xml；
# request 中的body数据不能重复读取，若重复读取会报错
def body_data(request):
    # post 是表单的请求
    response = request.POST
    print(f'Post提取的类型:{type(response)}')
    print(f'Post提取的值：{response}')
    # Post提取的类型:<class 'django.http.request.QueryDict'>
    # Post提取的值：<QueryDict: {'username': ['abby'], 'password': ['123']}>

    # body是body中文字的请求，包括JSON
    response2 = request.body.decode()
    print(f'Body提取的类型:{type(response2)}')
    print(f'Body提取的值：{response2}')
    # Body提取的类型:<class 'str'>
    # Body提取的值：你好吗
    # JSON请求：
    # Body提取的类型:<class 'str'>
    # Body提取的值：{"name":"abby","age":12,"gender":"女"}
    return HttpResponse('body_data')


# 在http报文的头（header）中
def header_data(request):
    response = request.content_params
    response2 = request.content_type
    print(response)
    print(type(response))
    print(response2)
    print(type(response2))
    return HttpResponse('header_data')

# cookie
def set_get_cookies(request):
    # 如果第一次访问，设置cookie信息返回给浏览器
    get_cookie_name= request.COOKIES
    print(get_cookie_name)
    if not get_cookie_name:
        # cookie信息根据url中的字符串查询信息返回
        # cookie的格式：name=<username>,age=<age>
        username=request.GET.get('username')
        response = HttpResponse('第一次访问')
        response.set_cookie('name',username,max_age=2)
        return response
    else:

        response=f'非第一次访问，COOKIE为：{get_cookie_name}'
    # 如果已经访问过了，则返回浏览器响应的cookie信息打印在页面
        return HttpResponse(response)

