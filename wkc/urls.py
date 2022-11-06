from django.urls import path
from .views import WkcBookingTemplateView, Schedule,check_date_clash

urlpatterns = [
    path("wkc-booking/", WkcBookingTemplateView.as_view(), name="wkc_booking"),
    path("wkc-schedule/", Schedule.as_view(), name="wkc_schedule"),
    path("api/check-date-clash", check_date_clash, name="check_clash"),
]