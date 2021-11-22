from django.db import reset_queries
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

def add(request):
    res={"status":1,"msg":""}
    if request.method=="POST":
        name=request.POST.get("post_name")
        models.Sample.objects.create(name=name)
        res["status"]=0
        res["msg"]="success"
    return JsonResponse(res)