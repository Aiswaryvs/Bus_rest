from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Bus import serializers
from Bus.models import BusList
from Bus.serializers import BusSerializer,UserRegistrationSerializer
from rest_framework import permissions, authentication

# Create your views here.

class BusView(viewsets.ModelViewSet):
    serializer_class = BusSerializer
    queryset = BusList.objects.all()
    model = BusList
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg:Registration Successfull'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

