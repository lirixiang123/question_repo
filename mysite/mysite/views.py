from django.shortcuts import HttpResponse,render
import logging
logger=logging.getLogger('apis')
def logtest(request):
    logging.info("欢迎您")
    print("cccc")
    return HttpResponse("日志测试")
def test(request):
    return render(request,'test.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.repo.models import Questions
def paginator(request):
    objects=Questions.objects.all()
    p=Paginator(objects,25)
    page=request.GET.get('page')

    contacts =p.page(page)

    return render(request,'paginator.html',locals())