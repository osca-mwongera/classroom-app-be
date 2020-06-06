from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from accounts.models import Profile


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
        fields = UserDetailsSerializer.Meta.fields + (
            'avatar', 'phone_number', 'is_tutor')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance = super(ProfileSerializer, self).update(instance, validated_data)

        profile = instance.profile
        if profile_data:
            if profile_data.get('avatar'): profile.avatar = profile_data.get('avatar')
            if profile_data.get('phone_number'): profile.phone_number = profile_data.get('phone_number')
            if profile_data.get('is_tutor'): profile.is_realtor = profile_data.get('is_tutor')
            profile.save()

        return instance
