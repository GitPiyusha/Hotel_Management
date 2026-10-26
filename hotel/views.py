from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HotelModel
from .serializer import HotelSerializer


class HotelApiView(APIView):
    def get(self, request):
        hotels = HotelModel.objects.all()
        serializer = HotelSerializer(hotels, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)