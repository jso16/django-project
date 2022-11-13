from django.shortcuts import render
from django.http import HttpResponse
from .models import EmailNewsletter


def index(request):
    latest_email_list=EmailNewsletter.objects.order_by('-registred_at')
   
    return render(request, 'page/index.html',
    {
        "latest_email_list":latest_email_list   
    })
