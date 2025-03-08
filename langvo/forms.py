from django import forms
from langvo.models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Inquiry
        # InquiryForm에서 사용할 Inquiry 모델의 속성
        fields = ['inq_email', 'inq_title', 'inq_content', 'inq_category'] 
        # labels = {
        #     'inq_email': '답변을 받을 이메일',
        #     'inq_title': '문의 제목',
        #     'inq_content': '문의 내용',
        #     'inq_category': '문의 카테고리',
        # }