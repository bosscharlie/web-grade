from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models
# Create your views here.
def show(request):
    res={"status":0,"msg":""}
    try:
        test=models.Sample.objects.filter()
    except Exception as e:
        res["msg"]=str(e)
        res["status"]=1
    return JsonResponse(res)
