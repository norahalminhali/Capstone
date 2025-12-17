from django.urls import path

from . import views


app_name = "trips"


urlpatterns=[
path('create/', views.create_trip_view, name='create_trip_view'),
]