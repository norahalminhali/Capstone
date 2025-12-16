from django.db import models
from django.contrib.auth.models import User
#import city from main
#import driver from driver


# Create your models here.

class Rider (models.Model):

    #Gender
    class Gender (models.TextChoices):
        F = "female", "Female"
        M = "male", "Male"

    #Car size
    class SizeCarName (models.TextChoices):
        S = "small", "Small"
        M = "medium", "Medium"
        L = "larg", "Larg"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    national_id_or_iqama = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.F)
    avatar = models.ImageField(upload_to="images/avatars/",default="images/avatars/avatar.webp")
    date_of_birth = models.DateTimeField(auto_now_add=False)

    size_car = models.CharField(max_length=64, choices=SizeCarName.choices, default=SizeCarName.M)
    #cities = models.ManyToManyField(City)

class ReviewRider (models.Model):

    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    #driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    comments = models.TextField()

    #created_at = models.DateTimeField(auto_now_add=True)