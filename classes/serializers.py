from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Lesson
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
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return Lesson.objects.create(owner=user, **validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data['category']
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.comments_enabled = validated_data['comments_enabled']
        instance.file = validated_data['file']
        instance.tags = validated_data['tags']
        instance.save()
        return instance
