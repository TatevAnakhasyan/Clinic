from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name = 'home'),
    path('404/', FourListView.as_view(), name = 'four'),
    path('about/', AboutListView.as_view(), name = 'about'),
    path('appointment/', AppointmentListView.as_view(), name = 'appo'),
    path('contact/', ContactListView.as_view(), name = 'contact'),
    path('feature/', FeatureListView.as_view(), name = 'feature'),
    path('service/', ServiceListView.as_view(), name = 'service'),
    path('team/', TeamListView.as_view(), name = 'team'),
    path('testimonial/', TestimonialListView.as_view(), name = 'test'),

]