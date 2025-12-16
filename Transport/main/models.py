from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="hoods")
    
    def __str__(self):
        return self.name 

class Day(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name