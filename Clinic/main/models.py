import PIL
import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from datetime import datetime





class AboutStore(models.Model):
    address = models.CharField('Address', max_length=100)
    email = models.EmailField('Email')
    phone = PhoneNumberField()

    facebook = models.URLField('Facebook URL', blank=True)
    twitter = models.URLField('Twitter URL', blank=True)
    linkedin = models.URLField('Linkedin URL', blank=True)
    instagram = models.URLField('Instagram URL', blank=True)
    youtube = models.URLField('Youtube', blank=True)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'About Store'
        verbose_name_plural = 'About Stores'


class Header(models.Model):
    aboutstore = models.ForeignKey(AboutStore, on_delete=models.CASCADE, related_name='aboutheder', null=True)
    text = models.CharField('Time', max_length=50, null=True)

    def __str__(self) -> str:
        return f"Header"
    
    class Meta:
        verbose_name = 'Header Info'
        verbose_name_plural = 'Headers Infos'


class Pages(models.Model):
    name = models.CharField('Name', max_length=20)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class GeneralSliderL(models.Model):
    title = models.CharField('Title', max_length=100)
    doctors = models.SmallIntegerField('Expert Doctors')
    stuff = models.SmallIntegerField('Medical Stuff')
    patients  = models.SmallIntegerField('Total Patients')

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        verbose_name = 'General Slider  Left'
        verbose_name_plural = 'General Slider  Left'
        

class GeneralSliderR(models.Model):
    title = models.CharField('Title', max_length=20)
    img = models.ImageField('Image', upload_to='media' )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'General Slider Right'
        verbose_name_plural = 'General Sliders Right'


class AboutUs(models.Model):
    title = models.CharField('Title', max_length=255)
    text1 = models.TextField('First Text', max_length=255)
    text2 = models.TextField('Second Text', max_length=255)
    note1 =  models.CharField('First Note', max_length=50)
    note2 =  models.CharField('Second Note', max_length=50)
    note3 =  models.CharField('Third Note', max_length=50)
    img1 = models.ImageField('First Image', upload_to='media')
    img2 = models.ImageField('Second Image', upload_to='media')

    def __str__(self) -> str:
        return ' '.join(self.title.split()[:3])
    
    class Meta:
        verbose_name = 'About Us'  
        verbose_name_plural = 'About Uses'


class OurDoctors(models.Model):
    aboutstore = models.ForeignKey(AboutStore, on_delete=models.CASCADE, related_name='doc', null=True)
    img = models.ImageField('Image', upload_to='media')
    name = models.CharField('Name', max_length=50)
    department = models.CharField('Department', max_length=100)
    
   
                                   
    def __str__(self) -> str:
        return self.name
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "60"/>')
    

    class Meta:
        ordering = ['name']
        verbose_name = 'Our Doctor'
        verbose_name_plural = 'Our Doctors'


class ContactUs(models.Model):
    name = models.CharField('Name' , max_length=100)
    email = models.EmailField('Email')
    subject = models.CharField('Subject' , max_length=250)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class Query(models.Model):
    text = models.TextField('Query')

    def __str__(self) -> str:
        return ' '.join(self.text.split()[:3])

    class Meta:
        verbose_name = 'Any Query'
        verbose_name_plural = 'Any Queries'


class Service(models.Model):
    title = models.CharField('Title', max_length=20)
    text = models.TextField('Text', max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

  
class Feature(models.Model):
    title = models.CharField('Title', max_length=20)
    text = models.TextField('Text', max_length=255)
    note1 = models.CharField('Note 1', max_length=20)
    note2 = models.CharField('Note 2', max_length=20)
    note3 = models.CharField('Note 3', max_length=20)
    note4 = models.CharField('Note 4', max_length=20)
    img = models.ImageField('Image', upload_to='media', null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='appuser', null=True)
    name = models.CharField('Name', max_length=60, blank=False, null=True)
    email = models.EmailField('Email', null=True)
    phone = PhoneNumberField('Phone number', null=True)
    doctor = models.ForeignKey(OurDoctors, on_delete=models.PROTECT, related_name='appodoc', null =True) 
    date = models.DateTimeField('Date  of the appointment', auto_now_add=True, null=True)
    time = models.DateTimeField('Time of the appointment', auto_now_add=True, null=True)
    message = models.TextField('Message', max_length=255, null=True)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


class SlidApp(models.Model):
    image = models.ImageField('Slide Image', upload_to='media')
    
    def __str__(self) -> str:
        return f"Slider"
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'


class AppUs(models.Model):
    aboutstore = models.ForeignKey(AboutStore, on_delete=models.CASCADE, related_name='appus')
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Visit Our Doctor'
        verbose_name_plural = 'Visit Our Doctor'


class Testimonial(models.Model):
    img = models.ImageField('Image', upload_to='media')
    text = models.TextField('Text', max_length=255)
    name = models.CharField('Patient Name', max_length=50)
    profession = models.CharField('Profession', max_length=50)

    def __str__(self) -> str:
        return self.name
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "60"/>')
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'


class PageTitle(models.Model):
    title = models.CharField('Title', max_length =50)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Page Title'
        verbose_name_plural = 'Page Titles'


class Newsletter(models.Model):
    email = models.EmailField('Email')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'