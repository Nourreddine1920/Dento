from email import message
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
        return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'message from ' + message_name +" / email : " +  message_email,  # subject
            message,  # message
            message_email,  # from email
            ['nourreddine2000@gmail.com'],
            fail_silently=False  # whome email
        )

        return render(request, 'contact.html', {'message_name': message_name , 'message_email' : message_email})
    else:
        return render(request, 'contact.html')


def blog_details(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request , 'blog-details.html')

    else : 
        return render(request, 'blog-details.html')


def blog(request):
    return render(request, 'blog.html')


def index(request):
    return render(request, 'index-2.html')


def pricing(request):
    return render(request, 'pricing.html')


def service(request):
    return render(request, 'service.html')


def appointment(request):
    if request.method == "POST":

        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        appointment = "I am " + your_name + " with email : "+  your_email +  " I want an appointment in " + your_schedule + " on " + your_date 
        

        send_mail(
            'Appointment Request',  # subject
            appointment,  # message
            your_email,  # from email
            ['nourreddine2000@gmail.com']  # whome email
        )
        context = {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        }
        return render(request, 'appointment.html', context)
    else:
        return render(request, 'home.html')


