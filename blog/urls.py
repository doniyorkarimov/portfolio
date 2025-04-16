from django.urls import path
from .views import BLogListView, BlogDetailView



urlpatterns = [
    path('blogs/', BLogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail')
]