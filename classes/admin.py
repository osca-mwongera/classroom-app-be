from django.contrib import admin
from .models import Category, Lesson


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'category', 'name', 'description', 'comments_enabled', 'file', 'tag_list', 'date_uploaded', 'owner'
    ]
    # fieldsets = (
    #     (None, {'fields': ('tags',)}),
    # )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
