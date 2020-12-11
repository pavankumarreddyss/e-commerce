from django.shortcuts import render
from songs.models import Movie,Audio,Video
from django.db.models import Q
from songs.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def movies(request):
    mlist=Movie.objects.all()
    return render(request,'movies.html',{'mlist':mlist})

def movie_details(request,x):
    m=Movie.objects.get(id=x)
    lst1=Audio.objects.filter(movie=m)
    lst2=Video.objects.filter(movie=m)
    return render(request,'movie_details.html',{'m':m,'lst1':lst1,'lst2':lst2})

def audios(request):
    alist=Audio.objects.all()
    return render(request,'audios.html',{'alist':alist})

def videos(request):
    vlist=Video.objects.all()
    return render(request,'videos.html',{'vlist':vlist})

def search_list(request):
    q=request.GET.get('query')
    if q:
        match1=Movie.objects.filter(Q(title__icontains=q)|Q(director__icontains=q))
        match2=Audio.objects.filter(Q(title__icontains=q))
        match3=Video.objects.filter(Q(title__icontains=q))
        if match1 or match2 or match3:
           return render(request,'search_list.html',{'match1':match1,'match2':match2,'match3':match3})
    else:
        return HttpResponseRedirect('/search_list')
    return render(request,'search_list.html')

def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        subject='message from freesongs.com'
        message=request.POST.get('content')
        user_email=request.POST.get('content_email')
        from_email=settings.EMAIL_HOST_USER
        to_list=[user_email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})  

def thankyou(request):
    res=HttpResponse()
    res.write("<h2>thanks for contacting freesongs.com</h2>")
    res.write("<br><h2>we just sent a mail to you</h2>")
    return res  