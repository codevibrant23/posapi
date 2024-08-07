from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomUserSerializer

@swagger_auto_schema(
    method='post',
    request_body=CustomUserSerializer,
    responses={
        201: openapi.Response(
            description="User created successfully.",
            examples={
                "application/json": {
                    "message": "User created successfully."
                }
            }
        ),
        400: openapi.Response(
            description="Invalid input.",
            examples={
                "application/json": {
                    "username": ["This field is required."],
                    "password": ["This field is required."],
                    # Include other potential errors based on your validation
                }
            }
        ),
    }
)
@api_view(['POST'])
def user_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
