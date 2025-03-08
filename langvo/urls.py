from django.urls import path

from . import views

# 서로 다른 앱에서 동일한 URL 별칭을 사용하면 중복 문제가 발생하기 때문에 namespace를 지정하는 app_name변수를 추가
app_name = 'langvo'

urlpatterns = [
    path('', views.index, name='index'), # config/urls에서 이미 langvo/로 시작하는 url이 매핑되었기 때문에 langvo/ + '' 이 되는 것
    path('<int:inq_id>/', views.detail, name='detail'), # 문의 상세보기
    path('inquiry/create/', views.create, name='inquiry_create'), # 문의 생성하기
    path('inquiry/success/', views.success, name='inquiry_success'), # 문의 성공페이지
]