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
        print(request.data, "request.data")
        serializer = LessonSerializer(data=request.data, many=False, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        for key, value in serializer.errors.items():
            for error in value:
                return Response({'details': error}, status=status.HTTP_400_BAD_REQUEST)
