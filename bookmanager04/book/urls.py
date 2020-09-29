from django.urls import path

from book.views import weather, login, body_data, header_data, set_get_cookies

urlpatterns=[
    path('weather/<city>/<year>/',weather),
    path('login/',login),
    path('body_data/',body_data),
    path('header_data/',header_data),
    path('set_get_cookies/',set_get_cookies),
]