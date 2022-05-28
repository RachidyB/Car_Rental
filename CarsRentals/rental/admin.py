from django.contrib import admin
from rental.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Reservation)

