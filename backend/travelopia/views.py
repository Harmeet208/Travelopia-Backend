import json
from django.views import View
from django.http import JsonResponse
from travelopia.models import TravellerDetails
from travelopia.exceptions import *
from travelopia.validations import validate_create_traveller_data

class MyView(View):
    def get(self, request):
        traveller_details = TravellerDetails.objects.all().order_by('-id')
        traveller_details_list = []
        for traveller_detail in traveller_details:
            traveller_details_list.append({
                'name': traveller_detail.name,
                'email': traveller_detail.email,
                'budget_per_person': traveller_detail.budget_per_person,
                'number_of_traveller': traveller_detail.number_of_traveller,
                'destination_country': traveller_detail.destination_country
            })
        print(f"traveller_details_list: {traveller_details_list}")
        response = JsonResponse({'data': traveller_details_list}, status=200)
        return response

    def post(self, request):
        request_data = json.loads(request.body)
        try:
            validate_create_traveller_data(request_data)
            traveller_obj = TravellerDetails.objects.create(**request_data)
            traveller_obj.save()
        except (InvalidNumberOfTravellerException, InvalidBudgetPerPersonException, 
                InvalidDestinationCountryException, InvalidNameException, InvalidEmailException) as e:
            return JsonResponse({'message': str(e.args[0]), 'code': 400}, status=400)
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            return JsonResponse({'message':'Internal Server Error', 'code': 500}, status=500)

        return JsonResponse({'message':'Data Submitted Successfully', 'code': 200}, status=200)