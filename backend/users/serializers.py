from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import get_user_model
from organizations.models import Organization

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    organization_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)

    def create(self, validated_data):
        with transaction.atomic():
            # Create organization
            organization = Organization.objects.create(
                name=validated_data["organization_name"]
            )

            # Create admin user
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
                role=User.Role.ADMIN,
                organization=organization,
            )

            return user
