from django.db import models
from django.contrib.auth.models import User
from main.models import City
from drivers.models import Driver
from django.core.validators import RegexValidator



# Create your models here.

class Rider (models.Model):

    #validator Phone
    phone_regex = RegexValidator(
        regex=r'^(9665\d{8}|05\d{8})$',
        message="Phone number must be in format: '9665********' or '05********' (10 digits). Only digits allowed."
    )
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
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    national_id_or_iqama = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.F)
    avatar = models.ImageField(upload_to="images/avatars/",default="images/avatars/avatar.webp")
    date_of_birth = models.DateField()

    size_car = models.CharField(max_length=64, choices=SizeCarName.choices, default=SizeCarName.M)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username 

class ReviewRider (models.Model):

    class RatingChoices(models.IntegerChoices):
        ONE = 1, '1 Star'
        TWO = 2, '2 Stars'
        THREE = 3, '3 Stars'
        FOUR = 4, '4 Stars'
        FIVE = 5, '5 Stars'

    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE, related_name="rider_reviews")
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.THREE)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # لضمان عدم قيام السائق بتقييم نفس الراكب أكثر من مرة لنفس الرحلة
    class Meta:
        unique_together = ('trip', 'rider', 'driver')
    
    def __str__(self):
        return f"Review by {self.driver} for {self.rider} - Trip {self.trip.id}"