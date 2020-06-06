from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers
from rest_auth.serializers import UserDetailsSerializer

from accounts.models import Profile
from geodata.models import POI
from payments.models import Payment, PaymentType
from properties.models import Category, Property, Facility


class RealtorSerializer(serializers.ModelSerializer):
	fullname = serializers.CharField(read_only=True)
	email = serializers.CharField(read_only=True)

	class Meta:
		model = Profile
		exclude = ['user', 'created', 'updated', 'is_realtor']


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		exclude = ['id', 'slug']


class FacilitySerializer(serializers.ModelSerializer):

	class Meta:
		model = Facility
		fields = ['name',]


class PropertySerializer(geo_serializers.GeoFeatureModelSerializer):
	county = serializers.CharField(read_only=True)
	image_list = serializers.ListField(read_only=True)
	category_list = serializers.ListField(read_only=True)
	facility_list = serializers.ListField(read_only=True)

	class Meta:
		model = Property
		geo_field = 'location'
		exclude = ['created', 'updated', 'slug', 'realtor', 'facilities', 'categories']


class POISerializer(geo_serializers.GeoFeatureModelSerializer):

	class Meta:
		model = POI
		geo_field = 'location'
		exclude = ['created', 'updated']


class PaymentTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = PaymentType
		exclude = ['created', 'updated', 'slug']


class PaymentSerializer(serializers.ModelSerializer):
	payment_type = PaymentTypeSerializer()
	property_name = serializers.CharField(read_only=True)
	receipt_number = serializers.CharField(read_only=True)
	mpesa_amount = serializers.FloatField(read_only=True)

	class Meta:
		model = Payment
		exclude = ['transaction', 'client', 'property_item', 'checkout_request_id']


class PaymentCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Payment
		fields = ['property_item']


class ProfileSerializer(UserDetailsSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    gender = serializers.CharField(source='profile.gender')
    phone_number = serializers.CharField(source='profile.phone_number')
    alt_phone = serializers.CharField(source='profile.alt_phone')
    address = serializers.CharField(source='profile.address')
    zip_code = serializers.CharField(source='profile.zip_code')
    town = serializers.CharField(source='profile.town')
    region = serializers.CharField(source='profile.region')
    is_realtor = serializers.BooleanField(source='profile.is_realtor')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('avatar','gender','phone_number','alt_phone','address','zip_code','town','region','is_realtor')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance = super(ProfileSerializer, self).update(instance, validated_data)

        profile = instance.profile
        if profile_data:
            if profile_data.get('avatar'): profile.avatar = profile_data.get('avatar')
            if profile_data.get('gender'): profile.gender = profile_data.get('gender') 
            if profile_data.get('phone_number'): profile.phone_number = profile_data.get('phone_number')
            if profile_data.get('alt_phone'): profile.alt_phone = profile_data.get('alt_phone')
            if profile_data.get('address'): profile.address = profile_data.get('address')
            if profile_data.get('zip_code'): profile.zip_code = profile_data.get('zip_code')
            if profile_data.get('town'): profile.town = profile_data.get('town')
            if profile_data.get('region'): profile.region = profile_data.get('region')
            if profile_data.get('is_realtor'): profile.is_realtor = profile_data.get('is_realtor')
            profile.save()

        return instance
