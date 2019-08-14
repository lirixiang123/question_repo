from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.
def test(request):
    return HttpResponse("个人中心视图")

import logging
logger = logging.getLogger("account")

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "uc_profile.html")

    def post(self, request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            if request.POST.get("email"):
                request.user.email = request.POST.get("email")
            if request.POST.get("mobile"):
                print('change mobile')
                request.user.mobile = request.POST.get("mobile")
            if request.POST.get("qq"):
                request.user.qq = request.POST.get("qq")
            if request.POST.get("realname"):
                request.user.realname = request.POST.get("realname")
            request.user.save()
        except Exception as ex:
            ret_info = {"code": 200, "msg": "修改失败"}
        return render(request, "uc_profile.html", {"ret_info":ret_info})
from django.views.generic import View, ListView
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

class ChangePasswdView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "uc_change_passwd.html")

    def post(self, request):
        # from表单提交的数据
        old_password = request.POST.get("oldpassword")
        new_password1 = request.POST.get("newpassword1")
        new_password2 = request.POST.get("newpassword2")

        ## 前端验证 new_password1 == new_password2 才能提交

        if new_password1 != new_password2:
            ret_info = {"code":400, "msg":"新密码不一致"}
        else:
            user = auth.authenticate(username=request.user.username, password=old_password)
            if user:
                user.set_password(new_password1)
                user.save()
                auth.logout(request)
                # auth.update_session_auth_hash(request, user)
                ret_info = {"code":200, "msg":"修改成功"}
            else:
                ret_info = {"code": 400, "msg": "旧密码不正确"}
        return render(request, "uc_change_passwd.html", {"ret_info":ret_info})