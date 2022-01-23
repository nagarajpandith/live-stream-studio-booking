from django.urls import path
from .views import HomeTemplateView, BookingTemplateView, ManageBookingTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-a-booking/", BookingTemplateView.as_view(), name="booking"),
    path("manage-bookings/", ManageBookingTemplateView.as_view(), name="manage"),
]
