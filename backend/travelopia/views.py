from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
import json


class MyView(View):
    def get(self, request):
        db_res = Person.objects.all().order_by('-id')
        data = []
        for person in db_res:
            data.append({
                'name': person.name,
                'email': person.email,
                'currency': person.currency,
                'travellers': person.travellers,
                'country': person.country
            })
        print(f"data {data}")
        response = JsonResponse({'data': data}, status=200)
        return response

    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        response = JsonResponse({'message':'Success', 'code':200}, status=200)
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
        
        person = Person.objects.create(**data)
        person.save()

        return response