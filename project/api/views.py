from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ForwardEmail(APIView):
    def post(self, request, format=None):
        # Use Django mailer function to send email to website.guhyungm7gmail.com’
        # if email submission successful, send result back to client
        from_email = request.data.get('email', '')
        message = request.data.get('message', '')

        send_mail(
            subject = 'Message from <{}>'.format(from_email),
            message = message,
            from_email = 'website.guhyungm7@gmail.com',
            recipient_list = ['website.guhyungm7@gmail.com',],
            fail_silently = False
        )

        messages.add_message(
            request,
            messages.SUCCESS,
            'Email submitted successfully!',
            extra_tags='email')

        return render(request, "main/contacts.html")