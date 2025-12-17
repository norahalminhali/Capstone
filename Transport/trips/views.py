from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from drivers.models import Driver
from .forms import TripForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_trip_view(request:HttpRequest):
    try:
        driver = Driver.objects.get(user=request.user)
    except Driver.DoesNotExist:
        messages.error(request, "Must be driver to create trip")
        return redirect("/")

    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.driver = driver
            trip.save()
            form.save_m2m()
            messages.success(request, "Created Trip successfully", "alert-success")
            return redirect("/")
    else:
        form = TripForm()

    return render(request, "trips/create_trip.html",{"form":form}) 