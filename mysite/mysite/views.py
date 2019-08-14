from django.shortcuts import HttpResponse,render
import logging
logger=logging.getLogger('apis')
def logtest(request):
    logging.info("欢迎您")
    print("cccc")
    return HttpResponse("日志测试")
def test(request):
    return render(request,'test.html')