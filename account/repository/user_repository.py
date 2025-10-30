from django.contrib.auth.models import User


class UserRepository:

    @staticmethod
    def create(validated_data: dict) -> User:
        user = User.objects.create(**validated_data)
        return user