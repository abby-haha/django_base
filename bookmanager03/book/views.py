from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('index')


# http://127.0.0.1:8000/111/15627384920/?order=readcount&order=commentcount&gender=女
def shop(request,aa,bb):
    post = request.POST
    print(post) # 表单请求
    # <QueryDict: {'username': ['abby'], 'password': ['123']}>
    req_str= request.GET
    print(req_str)
    # < QueryDict: {'order': ['readcount', 'commentcount'], 'gender': ['女']} >
    print(req_str.get('order'))
    # commentcount
    print(req_str['gender'])
    # 女
    return HttpResponse('shop')

def register(request):
    # data = request.POST
    # print(data)
    # < QueryDict: {'username': ['itcast'], 'password': ['123']} >
    return HttpResponse('ok')

def json(request):
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

    response= HttpResponse('set_cookies')
    response.set_cookie('name','username')

    return response

def get_cookies(request):
    request = request.COOKIES.get('name')
    print(request)
    return HttpResponse('get_cookies')
