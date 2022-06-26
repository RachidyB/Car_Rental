from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rental.Views import Car
from rental.serializers import *

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Car Api

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('marque')
    serializer_class = CarSerializer


@api_view(['GET'])
def ShowAll(request):
    Cars = Car.objects.all()
    serializer = CarSerializer(Cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewCar(request, pk):
    Cars = Car.objects.get(matricule=pk)
    serializer = CarSerializer(Cars, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateCars(request):
    serializer = CarSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateCars(request, pk):
    Cars = Car.objects.get(matricule=pk)
    serializer = CarSerializer(instance=Cars, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCar(request, pk):
    Cars = Car.objects.get(matricule=pk)
    Cars.delete()

    return Response('Items delete successfully!')
