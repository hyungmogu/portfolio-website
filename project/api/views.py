from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ForwardEmail(APIView):
    def post(self, request, format=None):
        # On clicking submit, send email to backend
        # Validate email
        # Use Django mailer function to send email to ‘hyungmogu@gmail.com’
        # if email submission successful, send result back to client
        pass