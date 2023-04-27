from django.views import View
from django.http import HttpResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
import json


class MyView(View):
    def get(self, request):
        print(f"request {request}")
        response = HttpResponse('Hello, world!', status=200)
        response['Content-Type'] = 'text/plain'
        return response

    @csrf_exempt
    def post(self, request):
        # Do some processing here
        data = json.loads(request.body)
        response = HttpResponse('Success', status=200)
        response['Content-Type'] = 'text/plain'
        if not data.get('name'):
            response = HttpResponse('Please Provide Name', status=400)
            response['Content-Type'] = 'text/plain'
            return response

        if not data.get('email'):
            response = HttpResponse('Please Provide Email', status=400)
            response['Content-Type'] = 'text/plain'
            return response

        if not data.get('country'):
            response = HttpResponse('Please Provide Country', status=400)
            response['Content-Type'] = 'text/plain'
            return response

        if not data.get('currency'):
            response = HttpResponse('Please Provide Budget', status=400)
            response['Content-Type'] = 'text/plain'
            return response

        if not data.get('travellers'):
            response = HttpResponse('Please Provide Travellers', status=400)
            response['Content-Type'] = 'text/plain'
            return response
        
        person = Person(data)
        person.save()

        return response