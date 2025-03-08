# visualization/charts.py
# 시각화 관련 함수

import matplotlib.pyplot as plt
import numpy as np
import io
import base64

from django.db.models import Count
from wordcloud import WordCloud
from langvo.models import Inquiry

# 카테고리별 도넛 차트
def inquiry_donut_chart():
    # Inquiry 모델에서 각 문의 카테고리별 개수를 가져옴
    # values('inq_category') → 카테고리별 그룹화
    # annotate(count=Count('inq_id')) → 각 카테고리별 문의 개수 계산
    data = Inquiry.objects.values('inq_category').annotate(count=Count('inq_id'))
    # 위에서 만든 data를 이용해 카테고리와 개수를 리스트로 변환
    categories = [item['inq_category'] for item in data]
    counts = [item['count'] for item in data]

    # 카테고리와 개수를 쌍으로 묶고, 개수를 기준으로 정렬
    sorted_data = sorted(zip(categories, counts), key=lambda x: x[1], reverse=True)
    categories, counts = zip(*sorted_data)  # 다시 개별 리스트로 분리

    # 각 카테고리별 색상 지정
    colors = ['#FF5733', '#FFC300', '#33C1FF', '#4CAF50', '#9B59B6', '#7F8C8D']
    # 도넛 모양을 만들기 위한 설정
    # width → 안쪽을 얼마나 뚫어둘 것인가
    # edgecolor → 경계선 색
    # linewidth → 테두리 두께
    wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

    # plt.figure(figsize=(8, 8)) → 그래프 크기를 설정
    plt.figure(figsize=(8, 8))

    # plt.pie() → 파이 차트(도넛 차트) 생성
    wedges, texts, autotexts = plt.pie(
        counts,
        labels=categories,
        # autopct='%1.1f%%' → 퍼센트 표시
        autopct='%1.1f%%',
        # startangle=90 → 90도에서 시작
        startangle=90,
        # counterclock=False → 시계방향으로 그리기
        counterclock=False,
        colors=colors,
        # wedgeprops=wedgeprops → 도넛 형태 설정
        wedgeprops=wedgeprops,
        # textprops=dict() → 퍼센트 텍스트를 설정
        textprops=dict(color="w", fontsize=12, fontweight='bold')
    )

    plt.axis('equal')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    plt.close()  # 그래프 닫기

    graph = base64.b64encode(image_png).decode('utf-8')
    return graph

# 워드 클라우드
def inquiry_wordcloud():
    # Inquiry.objects.values_list('inq_content', flat=True)
    # → inq_content 필드만 가져와서 리스트 형태로 저장
    inquiries = Inquiry.objects.values_list('inq_content', flat=True)
    # ' '.join(inquiries)
    # → 모든 문의 내용을 하나의 문자열로 합침 (워드클라우드 생성에 필요)
    text = ' '.join(inquiries)

    # WordCloud(width=800, height=400, background_color='white')
    # → 가로 800px, 세로 400px 크기의 흰색 배경 워드클라우드 객체 생성
    # .generate(text)
    # → 합쳐진 문의 내용(text)을 기반으로 워드클라우드 생성
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # plt.figure(figsize=(10, 5) → 그래프 크기를 10x5로 설정
    plt.figure(figsize=(10, 5))
    # plt.imshow(wordcloud, interpolation='bilinear') → 생성된 워드클라우드를 이미지로 표시
    plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis('off') → x, y 축 제거 (깨끗한 화면을 위해)
    plt.axis('off')

    # io.BytesIO() → 메모리 버퍼 생성 (파일이 아닌 메모리에 저장)
    buffer = io.BytesIO()
    # plt.savefig(buffer, format='png') → 그래프를 PNG 이미지로 저장
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    plt.close()  # 그래프 닫기

    # image_png를 base64.b64encode()로 인코딩하여 웹에서 사용 가능하도록 변환
    graph = base64.b64encode(image_png).decode('utf-8')
    return graph