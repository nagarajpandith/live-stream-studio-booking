from statistics import mode
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Booking
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from datetime import timedelta
from django.shortcuts import render

class HomeTemplateView(TemplateView):
    template_name = "index.html"

class BookingTemplateView(TemplateView):
    template_name = "booking.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        end_date = request.POST.get("end_date")
        message = request.POST.get("request")
        #Checking if booking already exists in range of event_date to end_date + 30 mins
        #Checking for date : START : end_date : END
        q1 = Booking.objects.exclude(rejected=True).filter(event_date__lte=date).filter(end_date__gte=date)
        #Checking for START : date : END : end_date
        q2 = Booking.objects.exclude(rejected=True).filter(event_date__lte=end_date).filter(end_date__gte=end_date)
        #Checking for date: START : END : end_date
        q3=Booking.objects.exclude(rejected=True).filter(event_date__gte=date).filter(end_date__lte=end_date)

        #Avoiding booking time > 3 hours
        helper1 = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M')
        #st = helper1.time()
        sd = helper1.date()
        helper2 = datetime.datetime.strptime(end_date,'%Y-%m-%d %H:%M')
        #et = helper2.time()
        eed = helper2.date()
        # Create datetime objects for each time
        #helpert = datetime.datetime.combine(datetime.date.today(), et)
        #helpers = datetime.datetime.combine(datetime.date.today(), st)
        # Difference between datetimes 
        #diff = helpert - helpers
        # Difference in hours
        #diffh = diff.total_seconds() / 3600     

        #Avoiding invalid date inputs
        if date>=end_date:
            messages.add_message(request, messages.SUCCESS, f"Event start date cannot be after event end date. Please select a valid date.")
            return HttpResponseRedirect(request.path)

        #Avoiding invalid date inputs
        elif eed>sd:
            messages.add_message(request, messages.SUCCESS, f"Event should not exceed more than a day. Please select a valid date.")
            return HttpResponseRedirect(request.path)

        #Avoiding booking time > 3 hours
        #elif (diffh > 3):
            #messages.add_message(request, messages.SUCCESS, f"Event time should not exceed 2 hours. Please select a valid time.")
            #return HttpResponseRedirect(request.path)

        elif q1.count()==0 and q2.count()==0 and q3.count()==0:
            booking = Booking.objects.create(
            name=name,
            email=email,
            event_date=date,
            end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M") + timedelta(minutes=30),
            request=message,
            accepted=True,
            )
            booking.save()

            ed = booking.event_date
            # Converting DateTime object to str
            ed = datetime.datetime.strptime(ed,'%Y-%m-%d %H:%M')
            # Converting 24 hr to user friendly format
            ed = datetime.datetime.strftime(ed, '%d %B, %Y, %I:%M %p')

            # Removing 30 mins from end_date while mailing user
            # Already converted to string while adding timedelta
            end = booking.end_date - timedelta(minutes=30)
            # Converting to 12 hr format + removing date
            end = datetime.datetime.strftime(end, '%I:%M %p')

            data = {
            "name":name,
            "date":ed,
            "title":"Booking Confirmation",
            "message":f"Thank you for booking our Live Stream Studio. Your Event has been booked for the event: {booking.request} from {ed} to {end}."
            }
            message = get_template('email.html').render(data)

            email = EmailMessage(
                subject= f"Live Stream Studio Booking - Booking confirmed.",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[booking.email],
                reply_to=[email]
            )
            email.content_subtype = "html"
            email.send()
          
            messages.add_message(request, messages.SUCCESS, f"Booking successful on {ed} to {end} for the event : {booking.request} by {name}")
            return HttpResponseRedirect(request.path)

        else: 
            messages.add_message(request, messages.SUCCESS, f"We are extremely sorry {name}, the studio is not available on selected date and time.")
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
            "name":booking.name,
            "date":booking.event_date,
            "request":booking.request,
        }

        dform = booking.event_date
        # Converting 24 hr to user friendly format
        dform = datetime.datetime.strftime(dform, '%-d %B, %Y, %I:%M %p')

        # Removing 30 mins from end_date while mailing user
        fform = booking.end_date - timedelta(minutes=30)
        # Converting to 12 hr format + removing date
        fform = datetime.datetime.strftime(fform, '%I:%M %p')

        if request.POST:    
            # if '_accept' in request.POST:
            #     data["title"]="Booking Confirmation"
            #     data["message"]=f"Thank you for booking our Live Stream Studio. Your Event has been booked on for the event: {booking.request} from {booking.event_date} to {booking.end_date}."
            #     message = get_template('email.html').render(data)
            #     booking.accepted=True
            #     booking.save()
            #     email = EmailMessage(
            #     subject="Your live stream studio booking has been approved.",
            #     body=message,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[booking.email],
            #     )
            #     email.content_subtype = "html"
            #     email.send()
            #     messages.add_message(request, messages.SUCCESS, f"You accepted the booking request for {booking.request} by {booking.name} on {booking.event_date} to {booking.end_date}.")

                
            if '_reject' in request.POST:
                data["title"]="Booking Declined"
                data["message"]=f"Thank you for booking our Live Stream Studio. Unfortunately, Your booking had to be declined for the Event: {booking.request} on {dform} to {fform}, as {textReason}"
                message = get_template('email.html').render(data)
                booking.rejected=True
                booking.accepted=False
                booking.save()
                email = EmailMessage(
                subject= "Sorry, Your previously booked event at live stream studio booking has been declined.",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[booking.email],
                reply_to=[settings.EMAIL_HOST_USER]
                )
                email.content_subtype = "html"
                email.send()
                messages.add_message(request, messages.SUCCESS, f"You rejected the booking request for {booking.request} by {booking.name} on {dform} to {fform}")

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

        data = {
            "name":"Admin",
            "title":f"Message from {name}",
            "message":f"You have a message from {name}[{email}]-{message}"
        }
        Emessage = get_template('email.html').render(data)
        email = EmailMessage(
            subject= f"Live Stream Studio Booking - You have a message from {name}",
            body=Emessage,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.content_subtype = "html"
        email.send()
        return HttpResponseRedirect(request.path)

class Schedule(ListView):
    template_name = "schedule.html"
    model = Booking
    context_object_name = "schedule"
    login_required = True
    paginate_by = 10
    #Overriding get_queryset() to filter 
    def get_queryset(self):
        return Booking.objects.exclude(rejected=True).filter(event_date__gte=datetime.datetime.now()).order_by("event_date")
