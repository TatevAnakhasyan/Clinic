from django.contrib import admin
from .models import *


@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name', 'email']
    search_fields = ['id', 'name', 'email']
    
@admin.register(AboutUs)
class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'note1']
    list_display_links = ['title',  'note1' ]
    search_fields = ['title', 'note1' ]

@admin.register(OurDoctors)
class OurDoctorsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_preview']
    list_display_links = ['name']
    search_fields = ['name']
    readonly_fields = ['img_preview']

admin.site.register(GeneralSliderL)
admin.site.register(GeneralSliderR)
admin.site.register(Query)
admin.site.register(Header)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(Pages)
admin.site.register(AppUs)
admin.site.register(PageTitle)
admin.site.register(SlidApp)
admin.site.register(Newsletter)

@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'email']
    list_display_links = ['name', 'date', 'email']
    search_fields = ['name', 'date', 'email']

@admin.register(AboutStore)
class AboutStoreModelAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']
    list_display_links = ['address', 'phone', 'email']
    search_fields = ['address', 'phone', 'email']

@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['name',  'profession', 'img_preview' ]
    list_display_links = ['name', 'profession']
    search_fields = ['name', 'text', 'profession']
    readonly_fields = ['img_preview']


