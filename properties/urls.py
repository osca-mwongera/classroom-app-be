from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [

    path('', views.Home.as_view(), name='home'),

    path('map/', views.Map.as_view(), name='map_view'),

    path('property-list/', views.PropertyList.as_view(), name='property_list'),

    path('properties/<int:pk>/', views.PropertyDetail.as_view(), name='property_detail'),

    path('search/', views.SearchView.as_view(), name='search'),

]
