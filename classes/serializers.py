from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    date_added = serializers.DateField()

    # class Meta:
    #     fields = ['id', 'name', 'date_added']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        return instance


class LessonSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    category = CategorySerializer(many=False)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    comments_enabled = serializers.BooleanField(default=True)
    file = serializers.FileField()
    tags = TaggitSerializer()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        return instance
