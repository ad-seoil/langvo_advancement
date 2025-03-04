from django.db import models
from enum import Enum

# Create your models here.
# 문의 카테고리 정의
class InquiryCategory(Enum):
    REPORT_ABUSE = '신고합니다'
    ACCCOUNT_ACCESS = '계정 접근 불가'
    BUG_REPORT = '버그 신고'
    PURCHASE_ISSUE = '구매 또는 구독 문제'
    OTHER_BUG = '기타 버그'
    ACCOUNT_DELETION = '계정 삭제 요청'

# 문의 DB
class Inquiry(models.Model):
    inq_id = models.AutoField(primary_key=True)
    inq_email = models.EmailField()
    inq_title = models.CharField(max_length=200)
    inq_content = models.TextField()
    inq_category = models.CharField(
        max_length=20,
        # choices=[(category.name, category.value) 으로 인해서 화면단에는 category.name이 db에는 category.value가 저장된다
        choices=[(category.name, category.value) for category in InquiryCategory],
    )
    send_date = models.DateTimeField(auto_now_add=True)

    # id 값 대신 제목으로 표시
    def __str__(self):
        return self.inq_title
