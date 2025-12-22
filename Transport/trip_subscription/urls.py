from django.urls import path

from . import views


app_name = "trip_subscription"


urlpatterns=[
    path('trips/<int:join_trip_id>/checkout/',views.checkout_srtipe_view ,name="checkout_srtipe_view"),
    path('payment/success',views.payment_trip_success ,name="payment_trip_success"),
    path('payment/cancel',views.payment_trip_cancel ,name="payment_trip_cancel"),
]