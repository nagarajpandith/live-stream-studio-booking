from statistics import mode
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import WKCBooking
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# Check for date clash:
@csrf_exempt
def check_date_clash(request):
    body= json.loads(request.body.decode('utf-8'))
    date = body['date']
    end_date = body['end_date']
    # Checking if booking already exists in range of event_date to end_date
    # Checking for date : START : end_date : END
    q1 = WKCBooking.objects.filter(event_date__lte=date).filter(end_date__gte=date)
        # Checking for START : date : END : end_date
    q2 = WKCBooking.objects.filter(event_date__lte=end_date).filter(
            end_date__gte=end_date
        )
        # Checking for date: START : END : end_date
    q3 = WKCBooking.objects.filter(event_date__gte=date).filter(
            end_date__lte=end_date
        )

    if q1.count() != 0 or q2.count() != 0 or q3.count() != 0:
        return JsonResponse({"status": "error"})
    else:
        return JsonResponse({"status": "success"})

class WkcBookingTemplateView(TemplateView):
    template_name = "wkc_booking.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        end_date = request.POST.get("end_date")
        message = request.POST.get("request")
        booking = WKCBooking.objects.create(
                name=name,
                email=email,
                event_date=date,
                end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d"),
                request=message,
            )
        booking.save()

        # ed = booking.event_date
        #     # Converting DateTime object to str
        # ed = datetime.datetime.strptime(ed, "%Y-%m-%d")
        #     # Converting 24 hr to user friendly format
        # # ed = datetime.datetime.strftime(ed, "%d %B, %Y, %I:%M %p")
        # end = booking.end_date
        #     # Converting to 12 hr format + removing date
        # end = datetime.datetime.strftime(end, "%Y-%m-%d")

            # data = {
            # "name":name,
            # "date":ed,
            # "title":"Booking Confirmation",
            # "message":f"Thank you for booking our WKC. Your Event has been booked for the event: {booking.request} from {ed} to {end}."
            # }
            # message = get_template('email.html').render(data)

            # email = EmailMessage(
            #     subject= f"WKC Booking - Booking confirmed.",
            #     body=message,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[booking.email],
            #     reply_to=[email]
            # )
            # email.content_subtype = "html"
            # email.send()

        messages.add_message(
                request,
                messages.SUCCESS,
                f"Booking successful on {date} to {end_date} for the event : {booking.request} by {name}",
            )
        return HttpResponseRedirect(request.path)


class Schedule(ListView):
    template_name = "wkc_schedule.html"
    model = WKCBooking
    context_object_name = "schedule"
    login_required = True
    paginate_by = 10
    # Overriding get_queryset() to filter
    def get_queryset(self):
        return WKCBooking.objects.filter(
            event_date__gte=datetime.datetime.now()
        ).order_by("event_date")

