from django.urls import path
from .Views import Customers, Car, Reservation

urlpatterns = [
    # Customer
    path('Customer-list/', Customers.ShowAll, name='Customer-list'),
    path('Customer-list-by-id/<int:pk>/', Customers.ViewCustomer, name='Customer-list-by-id'),
    path('Customer-list-by-email/<email>/', Customers.ViewCustomer, name='Customer-list-by-email'),
    path('Customer-create/', Customers.CreateCustomer, name='Customer-create'),
    path('Customer-update/<pk>/', Customers.updateCustomer, name='Customer-update'),
    path('Customer-delete/<pk>', Customers.deleteCustomer, name='Customer-delete'),
    # Car
    path('Car-list/', Car.ShowAll, name='Car-list'),
    path('Car-list-by-id/<int:pk>/', Car.ViewCar, name='Car-list-by-id'),
    path('Car-create/', Car.CreateCars, name='Car-create'),
    path('Car-update/<pk>/', Car.updateCars, name='Car-update'),
    path('Car-delete/<pk>', Car.deleteCar, name='Car-delete'),
    # Reservation
    path('Reservation-list/', Reservation.ShowAll, name='Reservation-list'),
    path('Reservation-list-by-id/<int:pk>/', Reservation.ViewReservation, name='Reservation-list-by-id'),
    path('Reservation-create/', Reservation.CreateReservation, name='Reservation-create'),
    path('Reservation-update/<pk>/', Reservation.updateReservation, name='Reservation-update'),

]
