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


#Customer API

@cache_page(CACHE_TTL)
@api_view(['GET'])
def ShowAll(request):
    Reservations = Reservation.objects.all()
    serializer = ReservationSerializer(Reservations, many=True)
    return Response(serializer.data)

@cache_page(CACHE_TTL)
@api_view(['GET'])
def ViewReservation(request, pk):
    Reservations = Customer.objects.get(id=pk)
    serializer = ReservationSerializer(Reservation, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateReservation(request):
    serializer = ReservationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateReservation(request, pk):
    Reservations = Reservation.objects.get(equipe_id=pk)
    serializer = ReservationSerializer(instance=Reservations, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteReservation(request, pk):
    Reservations = Reservation.objects.get(id=pk)
    Reservations.delete()

    return Response('Items delete successfully!')




