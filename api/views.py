from json import dumps

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import PropertySerializer, POISerializer, PaymentSerializer, PaymentCreateSerializer, RealtorSerializer
from properties.models import Property
from geodata.models import POI
from accounts.models import Profile
from payments.models import Payment, PaymentType
from payments.tasks import make_payment


class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer

class POIViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = POI.objects.all()
	serializer_class = POISerializer

class RealtorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Profile.objects.filter(is_realtor=True)
	serializer_class = RealtorSerializer

	@action(detail=False, methods=['get',], url_path='for_property/(?P<property_id>[^/.]+)')
	def for_property(self, request, property_id=None):
		property_item = Property.objects.get(pk=property_id)
		payments = Payment.objects.filter(client=request.user.profile, property_item=property_item)
		if payments:
			if payments.latest('timestamp').is_active:
				serializer = RealtorSerializer(property_item.realtor)
				return Response(serializer.data, status=status.HTTP_200_OK)

		data = dumps({'message': 'payment required to unlock realtor contact information'})
		return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class PaymentsApiView(ListCreateAPIView):

	def get_queryset(self):
		return Payment.objects.filter(client=self.request.user.profile)

	def get_serializer_class(self):
		if self.request.method == 'POST':
			return PaymentCreateSerializer
		return PaymentSerializer

	def perform_create(self, serializer):
		profile = self.request.user.profile
		payment_type = PaymentType.objects.get(slug='contact-unlock')  # Default payment is for unlocking realtor contacts
		obj = serializer.save(client=profile, payment_type=payment_type)
		make_payment.delay(obj.id, profile.id, payment_type.id)
