from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleListView(APIView):
    def get(self, request):
        return Response({"message": "RealNews API ishlayapti"})