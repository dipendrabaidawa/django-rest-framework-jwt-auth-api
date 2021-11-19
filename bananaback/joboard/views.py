from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
import json 
from django.db.utils import IntegrityError
from .models import CustomUser

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def register(request):
#     body = json.loads(request.body)
#     if body['password'] == body['confirm']:
#         try:
#             user = User.objects.create_user(username=body['username'], email=body['email'], password=make_password(body['password']))
#             return Response("Success", status=202)
#         except IntegrityError:
#             return Response("User already exists", status=401)            
#     else:
#         return Response("Passwords don't match", status=401)

def joboard(request):
    return render(request, "index.html")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print("!!!!!!!!!!!", attrs)
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@csrf_exempt
@api_view(['POST'])
def register(request):
    body = json.loads(request.body)
    if body['password'] == body['confirm_password']:
        try:
            print(body['first_name'])
            user = CustomUser(
                first_name=body['first_name'],
                last_name=body['last_name'],
                email=body['email'],
                username=body['email'].split('@')[0],
                date_joined = "2021-11-18T11:33:49.445+00:00",
            )
            user.set_password(body['password'])
            user.save()
                # password=make_password(body['password'])
            
            return Response("Success", status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response("User already exists", status=status.HTTP_401_UNAUTHORIZED)            
    else:
        return Response("Passwords don't match", status=status.HTTP_401_UNAUTHORIZED)


# class RegisterUserSerializer(serializers):
#     """Serializer for creating user objects."""
#     # tokens = serializers.SerializerMethodField()

#     def get_tokens(self, user):
#         tokens = RefreshToken.for_user(user)
#         refresh = str(tokens)
#         access = str(tokens.access_token)
#         data = {
#             "refresh": refresh,
#             "access": access
#         }
#         return data

#     def create(self, validated_data):
#         user = CustomUser(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

# def createuser(self, request, *args, **kwargs):
#         serializer = RegisterUserSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)