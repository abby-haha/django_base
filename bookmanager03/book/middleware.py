from django.utils.deprecation import MiddlewareMixin


class TextMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print('请求前被调用process_request')

    def process_response(self,request,response):
        print('响应前被调用process_response')
