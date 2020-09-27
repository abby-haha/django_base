from django.utils.deprecation import MiddlewareMixin


class TextMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print('1111请求前被调用process_request')

    def process_response(self,request,response):
        print('响应前被调用process_response11111')
        return response


class TextMiddleWare2(MiddlewareMixin):

    def process_request(self,request):
        print('22222请求前被调用process_request')

    def process_response(self,request,response):
        print('响应前被调用process_response22222')
        return response


# 执行顺序：
# 1111请求前被调用process_request
# 22222请求前被调用process_request
# 响应前被调用process_response22222
# 响应前被调用process_response11111