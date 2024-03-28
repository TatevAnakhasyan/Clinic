from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from .models import *
from django.http import Http404
from .forms import ContactUsForm
from .forms import AppointmentForm
from .forms import NewsletterForm
from django.core.mail import send_mail
from Clinic.settings import EMAIL_HOST_USER


class HomeListView(generic.ListView):
    template_name = 'index.html'
       
    @staticmethod
    def __extract_all_data():
      aboutstore = AboutStore.objects.get()
      generall = GeneralSliderL.objects.all()
      generalr = GeneralSliderR.objects.all()
      header = Header.objects.get()
      aboutus = AboutUs.objects.all()
      doctors = OurDoctors.objects.all()
      service = Service.objects.all()
      feature = Feature.objects.all()
      pages = Pages.objects.all()
      appus = AppUs.objects.all()
      test = Testimonial.objects.all()
      pagetitle = PageTitle.objects.get()
      

      context = {
         'nav':'home',
         'generall': generall,
         'generalr': generalr,
         'header': header,
         'aboutus': aboutus,
         'doctors': doctors,
         'aboutstore': aboutstore,
         'service': service,
         'feature': feature,
         'pages': pages,
         'appus': appus,
         'test':test,
         'pagetitle':pagetitle    
      }

      return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      
      context = self.__extract_all_data()
      
      return render(request, self.template_name, context=context)
    
    def post(self, request):
       
      context = self.__extract_all_data()

      form = NewsletterForm(request.POST)
      if form.is_valid():
         form.save()
      else:
         form = NewsletterForm()

      context.update({'form':form})

      return render(request, self.template_name, context=context) 
      

class FourListView(generic.ListView):
    template_name = 'four.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      header = Header.objects.ge()

      context = {
         'nav':'four',
         'header':header
      }
      
      return render(request, self.template_name, context=context)


class AboutListView(generic.ListView):
    template_name = 'about.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      aboutus = AboutUs.objects.all()
      doctors = OurDoctors.objects.all()
      header = Header.objects.get()
      feature = Feature.objects.all()
      aboutstore = AboutStore.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'about',
         'slidapp': slidapp,
         'aboutus': aboutus,
         'doctors': doctors,
         'header': header,
         'feature': feature,
         'aboutstore': aboutstore
      }
      
      return render(request, self.template_name, context=context)


class AppointmentListView(generic.ListView):

    template_name = 'appointment.html'

    @staticmethod
    def __extract_all_data():
      header = Header.objects.get()
      appointment = Appointment.objects.all
      appus = AppUs.objects.all()
      aboutstore = AboutStore.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'appointment',
         'header': header,
         'slidapp': slidapp,
         'appointment': appointment,
         'appus': appus,
         'aboutstore': aboutstore
      }

      return context
            
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

      context = self.__extract_all_data()
      
      return render(request, self.template_name, context=context)
    
    def post(self,request):
       
      context = self.__extract_all_data()

      form = AppointmentForm(request.POST)

      if form.is_valid():
          email = request.POST['email']

         #  send_mail(
         #     subject='Clinic FeedBack',
         #     message= 'Thanks For Review',
         #     from_email=EMAIL_HOST_USER,
         #     recipient_list=[email],
         #     fail_silently=False,
         #  )

          form.save()
      else:
         form = AppointmentForm()

      context.update({'form':form})

      return render(request, self.template_name, context=context)    


class ContactListView(generic.ListView):
    template_name = 'contact.html'

    @staticmethod
    def __extract_all_data():
      contact = ContactUs.objects.all()
      query = Query.objects.get()
      aboutstore = AboutStore.objects.get()
      header = Header.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'contact',
         'slidapp': slidapp,
         'contact': contact,
         'query': query,
         'aboutstore': aboutstore,
         'header': header
       }

      return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

      context = self.__extract_all_data()

      return render(request, self.template_name, context=context)

    def post(self,request):
       
      context = self.__extract_all_data()

      form = ContactUsForm(request.POST)

      if form.is_valid():
          email = request.POST['email']

          send_mail(
             subject='Clinic FeedBack',
             message= 'Thanks For Review',
             from_email=EMAIL_HOST_USER,
             recipient_list=[email],
             fail_silently=False,
          )

          form.save()
      else:
         form = ContactUsForm()

      context.update({'form':form})

      return render(request, self.template_name, context=context)    


class FeatureListView(generic.ListView):
    template_name = 'feature.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      header = Header.objects.get()
      feature = Feature.objects.all()
      aboutstore = AboutStore.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'feature',
         'header': header,
         'slidapp': slidapp,
         'feature': feature,
         'aboutstore': aboutstore
      }
      
      return render(request, self.template_name, context=context)


class ServiceListView(generic.ListView):
    template_name = 'service.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      header = Header.objects.get()
      service = Service.objects.all()
      aboutstore = AboutStore.objects.get()
      test = Testimonial.objects.all()
      pagetitle = PageTitle.objects.get()
      slidapp = SlidApp.objects.get()
      appointment = Appointment.objects.all()
      appus = AppUs.objects.all()

      context = {
         'nav': 'service',
         'header': header,
         'slidapp': slidapp,
         'service': service,
         'aboutstore':aboutstore,
         'test': test,
         'pagetitle': pagetitle,
         'appointment': appointment,
         'appus': appus
      }
      
      return render(request, self.template_name, context=context)  


class  TeamListView(generic.ListView):
    template_name = 'team.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      doctors = OurDoctors.objects.all()
      header = Header.objects.get()
      aboutstore = AboutStore.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'team',
         'slidapp': slidapp,
         'doctors': doctors,
         'header': header,
         'aboutstore': aboutstore 
      }
      
      return render(request, self.template_name, context=context)


class TestimonialListView(generic.ListView):
    template_name = 'testimonial.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
      header = Header.objects.get()
      aboutstore = AboutStore.objects.get()
      test = Testimonial.objects.all()
      pagetitle = PageTitle.objects.get()
      slidapp = SlidApp.objects.get()

      context = {
         'nav': 'testimonial',
         'header': header,
         'slidapp': slidapp,
         'aboutstore': aboutstore,
         'test': test,
         'pagetitle': pagetitle
      }
      
      return render(request, self.template_name, context=context) 


def error_404_view(request,exception):
   return render(request,'404.html')