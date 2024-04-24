from django.http import HttpResponse
from django.core.mail import send_mail

def send_email(request):
    send_mail(
        'Cadastro de Carros', 
        'Seu Carro registrado com sucesso',
        'jcmeseverino@gmail.com',
        ['gamerfrost8@gmail.com', 'jcmedeiros04@gmail.com'])
    return HttpResponse('RODOU CARAI')
