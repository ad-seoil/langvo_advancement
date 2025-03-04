# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Inquiry

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

# 메인 화면
def main(request):
    return render(request,'langvo/main.html')

# 문의 메일 화면
def show_inquiry_form(request):
    if request.method=='POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry_service = InquiryService()
            inquiry_service.send_email(form.cleaned_date)
            return redirect('inquiry_success')
        else:
            message.error(request,"문의 내용을 입력해주세요")
    else:
        form =InquiryForm()
    return render(request, 'inquiry_success.html')

# 문의 메일 리스트
def index(request):
    # 문의 목록 데이터는 Inquiry.objects.order_by('-send_date')로 얻을 수 있다
    # order_by('-send_date') 발송 시간을 역순으로 정렬 (-기호가 붙으면 역방향, 없으면 순방향 정렬)
    inquiry_list = Inquiry.objects.order_by('-send_date')
    context = {'inquiry_list' : inquiry_list}
    return render(request, 'langvo/inquiry_list.html', context)