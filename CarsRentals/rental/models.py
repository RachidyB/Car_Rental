
from django.db import models


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    dateN = models.DateField
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Car(models.Model):
    matricule = models.CharField(primary_key=True,max_length=20)
    marque = models.CharField(max_length=50)
    nombreCv = models.IntegerField()
    Serie = models.CharField(max_length=50)
    annee= models.IntegerField()
    prix_journaliser = models.FloatField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)
    image = models.ImageField(upload_to='image',null=True)

    def __str__(self):
        return self.marque


class Reservation(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.customer) + "- " + str(self.car)




# Create your models here.
