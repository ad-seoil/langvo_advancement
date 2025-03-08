# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inquiry
from .forms import InquiryForm

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def main(request):
    return render(request, 'langvo/main.html')

def index(request):
    # 문의 목록 데이터는 Inquiry.objects.order_by('-send_date')로 얻을 수 있다
    # order_by('-send_date') 발송 시간을 역순으로 정렬 (-기호가 붙으면 역방향, 없으면 순방향 정렬)
    inquiry_list = Inquiry.objects.order_by('-send_date')
    context = {'inquiry_list' : inquiry_list}
    return render(request, 'langvo/inquiry_list.html', context)

# 문의 상세보기 함수
def detail(request, inq_id):
    # get_object_or_404 를 쓰는 이유는 500에러가 뜨는 것보다 404에러가 뜨는 것이 더욱 바람직 하기 때문
    inquiry = get_object_or_404(Inquiry, pk=inq_id)
    context = {'inquiry':inquiry}
    return render(request, 'langvo/inquiry_detail.html', context)

# 문의 생성하기
def create(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        # 유효성 검사 실행
        if form.is_valid():
            # 새 inquiry 객체 생성
            # save()가 아닌 create()를 사용한 이유
            # save()는 객체를 명시적으로 생성한 후, 필요에 따라 수정한 후 저장할 수 있음 = 유연적임
            # create()는 간단하고 빠르게 객체를 생성하고 저장가능, 추가적인 수정이 필요할 경우 유연성이 떨어짐
            # -> 문의 메일은 수정할 필요가 없기 때문에 create()를 사용
            form.create()
            # 성공 후 성공페이지로 리다이렉트
            return redirect('langvo:inquiry_success')
    else:
        # GET 요청시 빈 폼을 생성
        form = InquiryForm()
    
    # 폼을 템플릿에 전달
    return render(request, 'langvo/inquiry.html', {'form':form})

def success(request):
    # 성공페이지 렌더링
    return render(request, 'langvo/inquiry_success.html')