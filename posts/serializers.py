from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')

class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'image', 'category', 'created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation