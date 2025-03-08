from django.urls import path
from . import views

app_name = 'visualization'

urlpatterns = [
    path('inquiry/visualization/', views.visualization_view, name='visualization'),
]
