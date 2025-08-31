from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    cart_id = serializers.SerializerMethodField()
    has_investor_details = serializers.SerializerMethodField()

    def get_cart_id(self, obj):
        cart = getattr(obj, "cart", None)
        return str(cart.id) if cart else None

    def get_has_investor_details(self, obj):
        return hasattr(obj, "investmenter_details")

    class Meta:
        model = User
        fields = (
            "uuid",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_picture",
            "is_staff",
            "is_superuser",
            "is_approvid",
            "user_type",
            "email_verified",
            "cart_id",
            "has_investor_details",
        )
