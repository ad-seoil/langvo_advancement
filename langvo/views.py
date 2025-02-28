# from django.http import HttpResponse
from django.shortcuts import render
from .models import Inquiry

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    # 문의 목록 데이터는 Inquiry.objects.order_by('-send_date')로 얻을 수 있다
    # order_by('-send_date') 발송 시간을 역순으로 정렬 (-기호가 붙으면 역방향, 없으면 순방향 정렬)
    inquiry_list = Inquiry.objects.order_by('-send_date')
    context = {'inquiry_list' : inquiry_list}
    return render(request, 'langvo/inquiry_list.html', context)