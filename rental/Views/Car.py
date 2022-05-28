import http
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rental.serializers import *
from rental.models import *
from rest_framework.response import Response

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


#Car Api

@cache_page(CACHE_TTL)
@api_view(['GET'])
def ShowAll(request):
    Cars = Car.objects.all()
    serializer = CarSerializer(Cars, many=True)
    return Response(serializer.data)

@cache_page(CACHE_TTL)
@api_view(['GET'])
def ViewCar(request, pk):
    Cars= Car.objects.get(matricule=pk)
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




