from .models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

class ArticleListCreateGenericAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer

class ArticleDetailGenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'