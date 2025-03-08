from django.urls import path
from . import views

app_name = 'visualization'

urlpatterns = [
    path('', views.visualization_view, name='visualization'),
]
