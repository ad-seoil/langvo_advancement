import json
from django.shortcuts import render
from langvo.models import Inquiry, InquiryCategory
from django.db.models import Count
from .charts import inquiry_donut_chart, inquiry_wordcloud

def visualization_view(request):
    # Inquiry 모델에서 각 문의 카테고리별 개수를 가져옴
    data = Inquiry.objects.values('inq_category').annotate(count=Count('inq_id'))
    
    # 카테고리와 개수를 리스트로 변환
    categories = [item['inq_category'] for item in data]
    counts = [item['count'] for item in data]
    
    # 카테고리 이름을 한국어로 변환
    korean_categories = [InquiryCategory[category].value for category in categories]
    
    # 카테고리와 개수를 쌍으로 묶고, 개수를 기준으로 정렬
    sorted_data = sorted(zip(korean_categories, counts), key=lambda x: x[1], reverse=True)
    korean_categories, counts = zip(*sorted_data)  # 다시 개별 리스트로 분리

    # JSON 형식으로 변환
    categories_json = json.dumps(korean_categories)
    counts_json = json.dumps(counts)

    donut_graph = inquiry_donut_chart()  # 도넛형 그래프 생성
    wordcloud_graph = inquiry_wordcloud()  # 워드클라우드 생성

    return render(request, 'visualization/visualizations.html', {
        'donut_graph': donut_graph,
        'wordcloud_graph': wordcloud_graph,
        'categories': categories_json,
        'counts': counts_json
    })
