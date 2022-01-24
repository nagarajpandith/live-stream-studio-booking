from .models import Booking

def get_notification(request):
    count = Booking.objects.filter(accepted=False).count()
    data = {
        "count":count
    }
    return data