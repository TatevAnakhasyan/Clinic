from django.forms import ModelForm
from .models import ContactUs
from .models import Appointment
from .models import Newsletter

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone',  'doctor',  'message']

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

