from django.db import reset_queries
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models
from django.core import serializers
import json
# Create your views here.
def show(request):
    res={"status":0,"msg":""}
    try:
        tests=models.Sample.objects.all()
        res['list']=json.loads(serializers.serialize("json",tests))
    except Exception as e:
        res["msg"]=str(e)
        res["status"]=1
    return JsonResponse(res)

def add(request):
    res={"status":1,"msg":""}
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get("post_name")
        test=models.Sample.objects.create(name=name)
        test.save()
        res["status"]=0
        res["msg"]="success"
    return JsonResponse(res)