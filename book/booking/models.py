from django.db import models


class Users(models.Model):
    From = models.CharField(max_length=50, blank=True)
    To = models.CharField(max_length=50, blank=True)
    Departure_date = models.DateField(blank=True)
    Return_date = models.DateField(blank=True)
    Class = models.CharField(max_length=30,blank=True)


    def __str__(self):
        return self.Class


