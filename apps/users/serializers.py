from rest_framework import serializers
from .models import UserModel
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .utlis import compress_image
from django.conf import settings
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'profile_image', 'total_experience', 'work_shift', 'designation')
        extra_kwargs = {
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        profile_image = attrs.get('profile_image')
        if profile_image:
            if profile_image.size > settings.MAX_IMAGE_UPLOAD:
                attrs['profile_image'] = compress_image(profile_image)
        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            profile_image=validated_data.get('profile_image'),
            total_experience=validated_data.get('total_experience'),
            work_shift=validated_data.get('work_shift'),
            designation=validated_data.get('designation'),

        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        response_data = super().to_representation(instance)
        response_data['token'] = token = Token.objects.get_or_create(user=instance)[
            0].key
        return response_data


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'profile_image',
                  'total_experience', 'work_shift', 'designation')

    def validate(self, attrs):
        profile_image = attrs.get('profile_image')
        if profile_image:
            if profile_image.size > settings.MAX_IMAGE_UPLOAD:
                attrs['profile_image'] = compress_image(profile_image)
        return attrs
