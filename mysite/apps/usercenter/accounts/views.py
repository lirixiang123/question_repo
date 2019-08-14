from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .forms import RegisterForm
# Create your views here.
def test(request):
    return HttpResponse("帐户视图")


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form":form})

    def post(self, request):
        pass
