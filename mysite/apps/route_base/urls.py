from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
#url(正则，视图，kws传递给视图的参数，name：为URL视图命名)
    #route_base

]