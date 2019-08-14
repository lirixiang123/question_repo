from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name="mobile_captcha")
]