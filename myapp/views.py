from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): # 첫 번째 파라미터의 인자로, 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달 받도록 되어있음.
    return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)