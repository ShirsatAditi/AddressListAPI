from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Address(models.Model):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100,null=True,)
    city = models.CharField(max_length=40,null=False)
    pin_code = models.IntegerField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.address_line1} - {self.address_line2} - {self.city} - {self.pin_code} - {self.user_id}"

    objects = models.Manager()
