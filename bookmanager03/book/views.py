from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


# Create your views here.
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


############################ cookies #############################
def set_cookies(request):
    response = HttpResponse('set_cookies')
    response.set_cookie('name', 'username')

    return response


def get_cookies(request):
    request = request.COOKIES.get('name')
    print(request)
    return HttpResponse('get_cookies')


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
    data= {'name':'abby','age':'11'}
    data_json=json.dumps(data)  # json.dumps():dict --> json   json.loads():json-->dict
    return HttpResponse(data_json)
    # return JsonResponse(data)

##############################

