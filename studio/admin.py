from django.contrib import admin
from .models import Booking
import csv
from django.http import HttpResponse

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    date_hierarchy = 'event_date'
    list_display = ("first_name", "last_name", "request", "event_date","email",)
    list_filter = ("event_date",)
    actions=['export_as_csv']
    def export_as_csv(ModelAdmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bookings.csv"'
        writer = csv.writer(response)
        writer.writerow(['Event Name', 'Event Date','First Name', 'Last Name', 'Email',])
        bookings = queryset.values_list('request', 'event_date','first_name', 'last_name', 'email',)
        for booking in bookings:
            writer.writerow(booking)
        return response
    export_as_csv.short_description = "Export Selected"

admin.site.register(Booking, BookingAdmin)
