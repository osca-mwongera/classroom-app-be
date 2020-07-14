from django.urls import path
from . import views

app_name = 'classes'
urlpatterns = [
    path('list-category', views.CategoryViewSet.as_view({'get': 'list'}), name='list_categories'),
    path('add-class', views.LessonView.as_view(), name='add_class'),
]
