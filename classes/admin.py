from django.contrib import admin
from .models import Category, Lesson


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'category', 'name', 'description', 'comments_enabled', 'file', 'tags', 'date_uploaded', 'owner'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
