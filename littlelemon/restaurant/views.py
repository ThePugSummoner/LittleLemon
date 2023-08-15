from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, status, viewsets, permissions

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World!')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



#class MenuView(APIView):
#    
#    def get(self, request):
#        items = Menu.objects.all()
#        serializer = MenuSerializer(items, many=True)
#        return Response(serializer.data)
#    
#    def post(self,request):
#        serializer = MenuSerializer(data=request.data)
#
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"status": "success", "data": serializer.data})
        
#class BookingView(APIView):
#    
#    def get(self, request):
#        items = Booking.objects.all()
#        serializer = BookingSerializer(items, many=True)
#        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer