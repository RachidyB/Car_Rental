from django.db import models


# Create your models here.
class user(models.Model):
    id = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.UserName
