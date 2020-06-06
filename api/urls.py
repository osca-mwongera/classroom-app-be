from django.urls import path, include
from rest_framework import routers
from rest_auth.views import UserDetailsView

from . views import PropertyViewSet, POIViewSet, PaymentsApiView, RealtorViewSet

router = routers.DefaultRouter()

router.register('properties', PropertyViewSet)
router.register('pois', POIViewSet)
router.register('realtors', RealtorViewSet)

urlpatterns = [

	path('auth/', include('rest_auth.urls')),

	path('auth/register/', include('rest_auth.registration.urls')),

	path('payments/', PaymentsApiView.as_view()),

]

urlpatterns += router.urls
