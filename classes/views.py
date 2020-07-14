from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer, LessonSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LessonView(APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def post(request):
        serializer = LessonSerializer(data=request.data, many=False, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
