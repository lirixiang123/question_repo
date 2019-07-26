from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
#url(正则，视图，kws传递给视图的参数，name：为URL视图命名)
    #route_base
    url(r'zoos/(\d+)/', views.zoos ,name='zoos1'),
    url(r'zoos/(?P<id>\d+)/', views.zoos2, name='zoos2'),
    url(r'zoos/(?P<id>\d+)/', views.zoos3,{"type":"dog"} ,name='zoos3'),
    url(r'^login/$',views.login,{"status":10},name='login')

]