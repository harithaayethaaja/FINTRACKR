from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import SignUpSerializer



class SignUpView(ModelViewSet):
    serializer_class = SignUpSerializer
    query_set = User.objects.all()