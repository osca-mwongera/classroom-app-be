from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Lesson
from .serializers import CategorySerializer, LessonSerializer


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LessonView(APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def post(request):
        serializer = LessonSerializer(data=request.data, many=False, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        for key, value in serializer.errors.items():
            for error in value:
                return Response({'details': error}, status=status.HTTP_400_BAD_REQUEST)


class TeacherClasses(APIView, StandardResultsSetPagination):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        queryset = Lesson.objects.filter(owner=self.request.user).order_by('-date_uploaded')
        paginated_results = self.paginate_queryset(queryset, request, view=self)
        serializer = LessonSerializer(paginated_results, many=True)
        return self.get_paginated_response(serializer.data)
