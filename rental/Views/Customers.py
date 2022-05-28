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
    Customers = Customer.objects.all()
    serializer = CustomerSerializer(Customers, many=True)
    return Response(serializer.data)

@cache_page(CACHE_TTL)
@api_view(['GET'])
def ViewCustomer(request, pk):
    Customers= Customer.objects.get(id=pk)
    serializer = CustomerSerializer(Customers, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateCustomer(request, pk):
    Customers = Customer.objects.get(equipe_id=pk)
    serializer = CustomerSerializer(instance=Customers, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCustomer(request, pk):
    Customers = Customer.objects.get(id=pk)
    Customers.delete()

    return Response('Items delete successfully!')




