from django import forms
from langvo.models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['inq_email', 'inq_title', 'inq_content', 'inq_category']