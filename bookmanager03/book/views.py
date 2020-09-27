from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


def index(request):
    return HttpResponse('index')


# http://127.0.0.1:8000/111/15627384920/?order=readcount&order=commentcount&gender=女
def shop(request, aa, bb):
    post = request.POST
    print(post)  # 表单请求
    # <QueryDict: {'username': ['abby'], 'password': ['123']}>
    req_str = request.GET
    print(req_str)
    # < QueryDict: {'order': ['readcount', 'commentcount'], 'gender': ['女']} >
    print(req_str.getlist('order'))
    # commentcount
    print(req_str['gender'])
    # 女
    return HttpResponse('shop')


def register(request):
    # data = request.POST
    # print(data)
    # < QueryDict: {'username': ['itcast'], 'password': ['123']} >
    return HttpResponse('ok')


def req_json(request):
    # body = request.body
    # print(body)
    # b'{\n\t"name":"itcast",\n\t"password":"123"\n}'
    # body_str=body.decode()
    # print(body_str)
    # {
    #     "name": "itcast",
    #     "password": "123"
    # }
    import json
    # body_dict =json.loads(body_str)
    # print(body_dict)
    # {'name': 'itcast', 'password': '123'}
    print(request.META)
    return HttpResponse('json')


def method(request):
    # print(request.method)
    # POST
    # GET
    return HttpResponse('method')


################################# 响应 #############################
def response(request):
    # HttpResponse(content响应体,状态码）
    # response = HttpResponse('这里是content部分页面显示内容',status=200)
    response = HttpResponse('这里是content部分页面显示内容')
    # 通过字典形式设置响应头的键值对
    response['host'] = '172.16.199.164'
    response['name'] = 'abby'
    # 也可通过字典形式设置状态码
    response.status_code = 200
    return response


import json


def response_json(request):
    data = {'name': 'abby', 'age': '11'}
    data_json = json.dumps(data)  # json.dumps():dict --> json   json.loads():json-->dict
    return HttpResponse(data_json)
    # return JsonResponse(data)


############################## 重定向 #################################
def redirect_url(request):
    return redirect('http://www.baidu.com')


############################ cookies #############################
def set_cookies(request):
    response = HttpResponse('set_cookies')  # 创建response对象
    response.set_cookie('name', '01')  # 对象.set_cookie
    return response


def get_cookies(request):
    cookie = request.COOKIES.get('name')
    print(cookie)
    return HttpResponse('get_cookies')


def set_get_cookies(request):
    cookie = request.COOKIES.get('name')
    if cookie:
        print(f'删除前：{cookie}')
        response = HttpResponse('已经访问过了')
        response.delete_cookie('name')

        print(f'删除后：{request.COOKIES.get("name")}')
        return response
    else:
        # set_cookies(request)
        print(f'第一次访问的cookie：{request.COOKIES.get("name")}')
        response = HttpResponse('第一次访问，服务器返回了cookie')  # 创建response对象
        response.set_cookie('name', '01', max_age=10)  # 对象.set_cookie
        return response


#######################  session ####################################3
def set_session(request):
    request.session['name'] = request.GET.get('username')
    request.session['pwd'] = request.GET.get('password')
    print(request.session['name'])
    print(request.session['pwd'])
    return HttpResponse('set_session')


def get_session(request):
    username = request.session.get('name')
    password = request.session.get('pwd')
    print(username, password)
    content = '{},{}'.format(username, password)
    return HttpResponse(content)


def del_session(request):
    request.session.clear()  # key（即session_id 还在，但是值已经没有了，网页的cookie还在）
    # request.session.flush()  # 键和值都没了，直接删除记录，网页的cookie删除了
    username = request.session.get('name')
    password = request.session.get('pwd')
    print(username, password)
    content = '{},{}'.format(username, password)
    return HttpResponse(content)


########################## 类视图 ###################################

class LoginView(View):
    def get(self, request):
        return HttpResponse('get get get')

    def post(self, request):
        return HttpResponse('post post post')


########################### 类视图的多继承 ############################
"""
我的订单、个人中心页面
如果登录用户 可以访问
如果未登录用户 不应该访问，应该跳转到登录页面

定义一个订单、个人中心 类视图

如果定义我有没有登录呢？？？ 我们以登录 后台站点为例
"""


class OrderView(LoginRequiredMixin,View):
    # as_view()里返回的是view函数
    # view函数返回的是self.dispatch()
    # 由于OrderView里没有重写dispatch函数，所以按照__mor__顺序调用父类的dispatch函数
    def get(self, request):
        return HttpResponse('已登录，get页面信息')

    def post(self, request):
        return HttpResponse('已登录，post页面信息')
