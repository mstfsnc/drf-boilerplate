from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from . import models
from . import serializers

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer