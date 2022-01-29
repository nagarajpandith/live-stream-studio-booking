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

class BookingTemplateView(TemplateView):
    template_name = "booking.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        date = request.POST.get("date")
        end_date = request.POST.get("end_date")
        message = request.POST.get("request")

        booking = Booking.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            event_date=date,
            end_date=end_date,
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
        textReason = request.POST.get("textReason")
        booking_id = request.POST.get("booking-id")
        booking = Booking.objects.get(id=booking_id)
        booking.accepted = False
        booking.accepted_date = datetime.datetime.now()
        booking.save()

        data = {
            "fname":booking.first_name,
            "date":booking.event_date,
            "request":booking.request,
        }

        if request.POST:    
            if '_accept' in request.POST:
                message = get_template('email.html').render(data)
                booking.accepted=True
                booking.save()
                email = EmailMessage(
                subject="About your Studio Booking",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[booking.email],
                )
                email.content_subtype = "html"
                email.send()
                
            elif '_reject' in request.POST:
                booking.rejected=True
                booking.save()
                email = EmailMessage(
                subject= f"About the Studio Booking.",
                body=f"Greetings {booking.first_name}. Unfortunately, your Booking had to be rejected due to {textReason}. Kindly book one more time.",
                from_email=settings.EMAIL_HOST_USER,
                to=[booking.email],
                reply_to=[settings.EMAIL_HOST_USER]
                )
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

class ContactUsTemplateView(TemplateView):
    template_name="contactUs.html"

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
        return HttpResponseRedirect(request.path)