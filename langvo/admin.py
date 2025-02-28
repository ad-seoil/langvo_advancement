from django.contrib import admin
from .models import Inquiry

# Register your models here.

# admin화면에서 제목으로 데이터를 검색할 수 있도록 설정
class InquiryAdmin(admin.ModelAdmin):
    search_fields = ['inq_title']

admin.site.register(Inquiry, InquiryAdmin)