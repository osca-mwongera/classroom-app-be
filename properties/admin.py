from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . models import Facility, Category, Property, Photo
from . forms import PropertyForm


class FacilityAdmin(admin.ModelAdmin):
	list_display = ['pk','name', 'property_count']
	list_display_links = ['name']


class PhotoInline(admin.TabularInline):
	model = Photo
	max_num = 10
	extra = 3


class PhotoAdmin(admin.ModelAdmin):
	list_display = ['pk', 'property_name', 'url', 'created']
	list_display_links = []


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'property_count']
	list_filter = ['name']
	prepopulated_fields = {'slug': ('name',)}


class PropertyAdmin(LeafletGeoAdmin):
	form = PropertyForm
	inlines = [PhotoInline]
	list_display = ['name','county','price_min','price_max','updated','is_available']
	list_filter = ['created', 'categories', 'price_max', 'is_available']
	list_editable = ['is_available', 'price_min', 'price_max']
	prepopulated_fields = {'slug': ('name',)}
	filter_horizontal = ['facilities', 'categories']

	def __init__(self, model, admin_site):
		super(PropertyAdmin, self).__init__(model,admin_site)
		self.form.admin_site = admin_site

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Photo, PhotoAdmin)
