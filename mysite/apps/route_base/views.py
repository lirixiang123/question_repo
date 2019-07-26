from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def login(request,status):
    if status==1:
        print(reverse("route_base:zoos3", args=(10,)))
        return redirect(reverse('route_base:index'))
    else:
        return HttpResponse("这是login页面")
def index(request):
    return HttpResponse('route_base index')
def zoos(request,zoo_id):
    return HttpResponse(f'{zoo_id}--zoos')
def zoos2(request,id):
    return HttpResponse(f'{id}--zoos')
def zoos3(request,id,type):
    return HttpResponse(f'{id}--zoos--{type}')