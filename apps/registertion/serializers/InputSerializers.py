from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    BooleanField,
    ImageField,
    ValidationError,
    EmailField,
)
from apps.Users.models import User, UserTypeChoice
from ..Tasks import serializers_tasks
from ..db_queries import services


class SignUpSerializer(ModelSerializer):
    profile_picture = ImageField(required=False)
    confirm_password = CharField(write_only=True, required=False)
    password = CharField(write_only=True, required=False)
    accept_terms = BooleanField(write_only=True, required=False)
    first_name = CharField(required=False)
    last_name = CharField(required=False)
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password",
            "email_verified",
            "profile_picture",
            "accept_terms",
            "user_type",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "username": {"read_only": True},
            "last_name": {"required": False},
            "first_name": {"required": False},
            "email": {"required": True},
            "user_type": {"required": True},
        }

    def validate_email(self, value: str):
        return serializers_tasks.validate_email(value, User)

    def validate_password(self, value: str):
        return serializers_tasks.validate_password_strength(value)

    def validate(self, data: dict):
        if data.get("user_type") == UserTypeChoice.INVESTOR and data.get("confirm_password") is None:
            raise ValidationError("Please add confirm password value.")

        if data.get("user_type") == UserTypeChoice.INVESTOR and data.get("password") != data.get(
            "confirm_password"
        ):
            raise ValidationError("Passwords do not match.")
        if data.get("user_type") == UserTypeChoice.INVESTOR and not data.get("accept_terms"):
            raise ValidationError("Terms and conditions must be accepted.")
        return data

    def create(self, validated_data: dict):
        return services.Create_user(validated_data)
