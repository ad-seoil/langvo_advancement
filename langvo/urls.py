from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # config/urls에서 이미 langvo/로 시작하는 url이 매핑되었기 때문에 langvo/ + '' 이 되는 것
]
