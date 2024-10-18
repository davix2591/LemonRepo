from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    

class SingleItemMenuView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 