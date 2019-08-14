from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from libs import sms
import random
import logging
logger = logging.getLogger("apis")

def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        # 获取ajax-用户提交的数据
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        # 生成随机验证码
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        # 将短信验证码写入redis, 300s 过期
        cache.set(mobile, mobile_captcha, 300)
        # 发送短信
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)