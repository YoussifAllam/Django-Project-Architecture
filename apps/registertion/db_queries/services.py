from apps.Users.models import User


def Create_user(validated_data: dict) -> User:
    user = User.objects.create_user(
        username=validated_data["email"],
        email=validated_data["email"],
        accept_terms=(validated_data["accept_terms"] if validated_data.get("accept_terms") else False),
        user_type=validated_data["user_type"],
        first_name=(validated_data.get("first_name") if validated_data.get("first_name") else ""),
        last_name=(validated_data.get("last_name") if validated_data.get("last_name") else ""),
    )
    if validated_data.get("password"):
        user.set_password(validated_data["password"])
        user.save()
    return user
