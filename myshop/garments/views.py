from django.shortcuts import render
from garments.models import FormalShirts
from garments.forms import ContactForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index (request):
    return render (request, 'index.html')
def aboutus(request):
    return render (request, 'aboutus.html')
def contactus(request):
    form = ContactForm
    if form.is_valid():
        subject = "hello from garments.com"
        message = "this is what you typed: " + request.post.get('content')
        from_email = settings.EMAIL_HOST_USER
        user_mail = requst.POST.get('contact_email')
        to_list = [user_email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fall_silently=False)
        return HttpResponseRedirect('Thankyou')
    return render (request, 'contactus.html', {'form' : form})
def formal_shirts(request):
    lst = FormalShirts.objects.all()
    return render (request, 'formal_shirts.html', {'lst' : lst })

def Thankyou(request):
    res = HttpResponse()
    res.write("<h1>thanks for visiting our site </h1>")
    res.write("<h1>we are in garments.com  </h1>")
    res.write("<h1> please go through site </h1>" )
    return res