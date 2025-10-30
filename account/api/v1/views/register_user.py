from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from account.repository.user_repository import UserRepository
from account.serializers import UserRegisterSerializer


class RegisterUser(viewsets.ViewSet):

    @extend_schema(request=UserRegisterSerializer,methods=["POST"])
    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        user = UserRepository.create(user_data)
        return Response({"user_id": user.id}, status=status.HTTP_201_CREATED)



