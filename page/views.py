from django.shortcuts import render
from django.http import HttpResponse
from .models import EmailNewsletter
from django.utils import timezone
from django.http import JsonResponse

def index(request):
    latest_email_list=EmailNewsletter.objects.order_by('-registred_at')
   
    return render(request, 'page/index.html',
    {
        "latest_email_list":latest_email_list   
    })


def register_email_newslatter(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        if email:
            verify = EmailNewsletter.objects.filter(email=email).exists()
            if verify:
                return JsonResponse({
                    'error': True,
                    'tag': 'repetido',
                    'msg' : 'Email já Cadastrado'
                })

            newslatter = EmailNewsletter(email=email, registred_at=timezone.now() )
            newslatter.save()
            return JsonResponse({
                'error': False,
                'tag': 'cadastrado',
                'msg' : 'Email Cadastrado com Sucesso'
            })
            print("teste")
    else:
        return JsonResponse({
            'error': True,
            'msg' : 'Método não permitido'
        })

