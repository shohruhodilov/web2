from django.urls import path
from .views import *

urlpatterns = [

    # path('', Qurilish_view.as_view(), name='home'),
    # path('send', sendjson, name='sendjson')
    path('hi/', hi, name='hi')


]
