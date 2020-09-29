from django.urls import path

from book.views import weather, login, body_data, header_data

urlpatterns=[
    path('weather/<city>/<year>/',weather),
    path('login/',login),
    path('body_data/',body_data),
    path('header_data/',header_data)
]