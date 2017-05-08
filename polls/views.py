from django.shortcuts import render

# Create your views here. 创建视图

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")