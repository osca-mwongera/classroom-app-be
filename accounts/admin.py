from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from . models import Profile

User = get_user_model()


class CustomUserAdmin(UserAdmin):
	pass


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['pk', 'fullname', 'phone_number', 'is_tutor', 'created', 'updated']
	list_display_links = ['fullname']
	list_filter = ['is_tutor']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
