from django.urls import path
from .views import (ArticleDetailGenericAPIView, ArticleListCreateGenericAPIView)

urlpatterns = [
    path('articles/', ArticleListCreateGenericAPIView.as_view()),
    path('articles/<slug:slug>/', ArticleDetailGenericAPIView.as_view() )
]