from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import *

from django.http import HttpResponse,JsonResponse

def base(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        contact_message=Contact()
        contact_message.name=name
        contact_message.email=email
        contact_message.phone=phone
        contact_message.subject=subject
        contact_message.message=message
        contact_message.submitted_at=timezone.now()
        contact_message.save()

        send_mail(
            subject='New Contact Form Submission',  # Subject of the email
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}',  # Email body
            from_email=email,  # From email address
            recipient_list=['info@agyglobaltrading.com'],  # List of recipients
            fail_silently=False,
        )

        return HttpResponse(f"<script>alert('Your message has been sent successfully!');window.location='/contact'</script>")
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def mining(request):
    return render(request, 'main/mining.html')
def equipment(request):
    return render(request, 'main/equipment.html')

def foodstuff(request):
    return render(request, 'main/foodstuff.html')

def sugar(request):
    return render(request, 'main/sugar.html')
def gold(request):
    return render(request, 'main/gold.html')
def gallery(request):
    return render(request, 'main/gallery.html')
def blogs(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'main/blogs.html', {'blog_posts': blog_posts})

def blog_detail(request, id):
    blog_post = get_object_or_404(BlogPost, id=id)
    return render(request, 'main/blog_detail.html', {'blog_post': blog_post})