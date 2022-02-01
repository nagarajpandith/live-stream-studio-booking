from django.urls import path
from .views import HomeTemplateView, BookingTemplateView, ManageBookingTemplateView, ContactUsTemplateView, Schedule
from django.contrib import admin
#Admin Cutomization
admin.site.site_header="Studio Booking"
admin.site.site_title= "Welcome to Studio Bookings"
admin.site.index_title = "Welcome to Studio Bookings Dashboard"

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("contact-us/", ContactUsTemplateView.as_view(), name="contact"),
    path("make-a-booking/", BookingTemplateView.as_view(), name="booking"),
    path("manage-bookings/", ManageBookingTemplateView.as_view(), name="manage"),
    path("view-schedule/", Schedule.as_view(), name="schedule"),
]

#handler404 = 'studio.dashboard.views.notfound'