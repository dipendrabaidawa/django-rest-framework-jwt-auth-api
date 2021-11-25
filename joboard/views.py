import json
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from .models import Candidate, CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
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

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response("Good bye!", status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

            return Response("Success", status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response("User already exists", status=status.HTTP_401_UNAUTHORIZED)            
    else:
        return Response("Passwords don't match", status=status.HTTP_401_UNAUTHORIZED)

def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()

class CandidatesView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        # perpage =  int(request.GET.get('perPage')) or None
        # curpage =  int(request.GET.get('curPage')) or None
        search = request.GET.get('search') or ""

        try:
            perpage =  int(request.GET.get('perPage'))
            curpage =  int(request.GET.get('curPage'))
        except ValueError:
            perpage = 0
            curpage = 0
            search = ""
        print(perpage, curpage, search)
        if perpage == 0 or curpage == 0:
            return Response(json.dumps({"candidates": [], "total": 0}, default = defaultconverter), status=200)    

        candidates = list(Candidate.objects.filter(title__contains=search).values())        
        total = len(candidates)
        return Response(json.dumps({"candidates": candidates[(curpage-1)*perpage:perpage*curpage], "total": total}, default = defaultconverter), status=200)

class CandidateDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, id):
        candidate = Candidate.objects.filter(id=id).values()[0]
        return Response(json.dumps(candidate, default=defaultconverter), status=200)
