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
        response = JsonResponse({'message':'Data Submitted Successfully', 'code': 200}, status=200)
        response['Content-Type'] = 'text/plain'
        if not data.get('name'):
            response = JsonResponse({'message':'Please Provide Name', 'code': 400}, status=400)
            return response

        if not data.get('email'):
            response = JsonResponse({'message':'Please Provide Email', 'code': 400}, status=400)
            return response


        if not data.get('country'):
            response = JsonResponse({'message':'Please Provide Country', 'code': 400}, status=400)
            return response


        if not data.get('currency'):
            response = JsonResponse({'message':'Please Provide Budget', 'code': 400}, status=400)
            return response

        if not data.get('travellers'):
            response = JsonResponse({'message':'Please Provide No of Trvellers', 'code': 400}, status=400)
            return response
        try:
            person = Person.objects.create(**data)
            person.save()
        except Exception as e:
            response = JsonResponse({'message':'Internal Server Error', 'code': 500}, status=500)
            return response

        return response