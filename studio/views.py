from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Booking
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from Live Stream Studio.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")


class BookingTemplateView(TemplateView):
    template_name = "booking.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        date = request.POST.get("date")
        message = request.POST.get("request")

        booking = Booking.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            event_date=date,
            request=message,
        )

        booking.save()

        email = EmailMessage(
            subject= f"{fname} from Live Stream Studio.",
            body=f"{fname} has booked Live Stream Studio on {date} for {message}. Login as Admin to confirm booking.",
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()

        messages.add_message(request, messages.SUCCESS, f"Thank you {fname} for booking the Studio, we will email you after confirmation! Your booked date is {date}.")
        return HttpResponseRedirect(request.path)

class ManageBookingTemplateView(ListView):
    template_name = "manage-bookings.html"
    model = Booking
    context_object_name = "bookings"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        booking_id = request.POST.get("booking-id")
        booking = Booking.objects.get(id=booking_id)
        booking.accepted = True
        booking.accepted_date = datetime.datetime.now()
        booking.save()

        data = {
            "fname":booking.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your Studio Booking",
            message,
            settings.EMAIL_HOST_USER,
            [booking.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the booking request of {booking.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        bookings = Booking.objects.all()
        context.update({   
            "title":"Manage Bookings"
        })
        return context
    #Custom 404
    def error_404(request, exception):
        return render(request, '404.html')