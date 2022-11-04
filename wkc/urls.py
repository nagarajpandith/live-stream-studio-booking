from django.urls import path
from .views import WkcBookingTemplateView, Schedule

urlpatterns = [
    path("wkc-booking/", WkcBookingTemplateView.as_view(), name="wkc_booking"),
    path("wkc-schedule/", Schedule.as_view(), name="wkc_schedule"),
]