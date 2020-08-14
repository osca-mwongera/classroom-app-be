from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class ProfileSerializer(UserDetailsSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    phone_number = serializers.CharField(source='profile.phone_number')
    is_tutor = serializers.BooleanField(source='profile.is_tutor')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('avatar', 'phone_number', 'is_tutor')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance = super(ProfileSerializer, self).update(instance, validated_data)
        profile = instance.profile
        print(validated_data, 'validated_data')
        if profile_data:
            if profile_data.get('avatar'):
                profile.avatar = profile_data.get('avatar')
            if profile_data.get('phone_number'):
                profile.phone_number = profile_data.get('phone_number')
            if profile_data.get('is_tutor'):
                profile.is_realtor = profile_data.get('is_tutor')
            profile.save()

        return instance
