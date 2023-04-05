from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def enviar_email(tipo, turma):
    email = EmailMessage(
        'Assunto do e-mail',
        f'Um novo {tipo} foi criado na turma {turma}',
        'suport.class.school@gmail.com',
        ['emersonnevess80@gmail.com'],
    )
    email.send()

