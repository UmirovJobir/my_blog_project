from django.core.mail import EmailMessage
from blog.celery import app


@app.task
def send_email(email, author, body):
    mail_subject = 'You have got a comment for your post'
    email = EmailMessage(mail_subject, author, body, to=[email])
    email.send()    