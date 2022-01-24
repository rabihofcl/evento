from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    _id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', '_id', 'category_name']

    def get__id(self, obj):
        return obj.id