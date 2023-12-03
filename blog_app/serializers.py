from rest_framework import serializers
from blog_app import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("title", "body", "author")