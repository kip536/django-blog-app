from rest_framework.views import APIView
from rest_framework.response import Response

from blog_app import models
from .serializers import PostSerializer

class PublicPostList(APIView):
    """Return the most recent public posts by all users"""
    def get(self, request):
        msgs = models.Post.objects.all()[:5]
        data = PostSerializer(msgs, many=True).data
        return Response(data)