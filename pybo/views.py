from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def index2(request):
    return HttpResponse("안녕하세요 pybo2에 오신것을 환영합니다.")

def hello(request):
    return HttpResponse("안녕하세요 hello 오신것을 환영합니다.")
def hello1(request):
    return HttpResponse("안녕하세요 hello1 오신것을 환영합니다.")
