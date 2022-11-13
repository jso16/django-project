from django.shortcuts import render
from django.http import HttpResponse
from .models import EmailNewsletter


def index(request):
    latest_email_list=EmailNewsletter.objects.order_by('-registred_at')
    output = ', '.join([q.email for q in latest_email_list])
    return HttpResponse(output)
