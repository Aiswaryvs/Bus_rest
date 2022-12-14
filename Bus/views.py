import email
from pydoc import visiblename
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Bus import serializers
from Bus.models import BusList, Reservation
from Bus.serializers import BusSerializer,UserRegistrationSerializer,UserLoginSerializer,BookingSerializer
from rest_framework import permissions, authentication
from django.contrib.auth import authenticate

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


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user =  authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg:Login Successfull'},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)                
            
# class PriceView(viewsets.ModelViewSet):
#     serializer_class = PriceSerializer
#     queryset = Price.objects.all()
#     model = Price
    # authentication_classes = [authentication.TokenAuthentication]
# permission_classes = [permissions.IsAuthenticated]    

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Reservation.objects.all()
    model = Reservation


