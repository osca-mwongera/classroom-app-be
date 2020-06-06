from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . models import County, POI


class CountyAdmin(LeafletGeoAdmin):
	pass


class POIAdmin(LeafletGeoAdmin):
	list_display = ['name', 'description', 'updated']


admin.site.register(County, CountyAdmin)
admin.site.register(POI, POIAdmin)
