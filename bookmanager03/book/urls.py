from django.urls import path

from book.views import index, shop

urlpatterns = [

    path('index/',index),
    path('<aa>/<bb>/',shop)
]
