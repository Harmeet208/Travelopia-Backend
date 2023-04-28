from travelopia.exceptions import *

def validate_create_traveller_data(request_data):
    if not request_data.get('name'):
        raise InvalidNameException('Please Provide Name')

    if not request_data.get('email'):
        raise InvalidEmailException('Please Provide Email')

    if not request_data.get('destination_country'):
        raise InvalidDestinationCountryException('Please Provide Destination Country')

    if not request_data.get('budget_per_person'):
        raise InvalidBudgetPerPersonException('Please Provide Budget Per Person')
    
    try:
        request_data['budget_per_person'] = int(request_data['budget_per_person'])
    except:
        raise InvalidBudgetPerPersonException('Enter Integer Value For Budget Per Person')    

    if int(request_data['budget_per_person']) <= 0:
        raise InvalidBudgetPerPersonException('Budget Per Person Cannot Be Less Than 1 USD')

    if not request_data.get('number_of_traveller'):
        raise InvalidNumberOfTravellerException('Please Provide Number of Travellers')
    
    try:
        request_data['number_of_traveller'] = int(request_data['number_of_traveller'])
    except:
        raise InvalidBudgetPerPersonException('Number Of Travellers Should Be Integer Value')    

    if int(request_data['number_of_traveller']) <= 0:
        raise InvalidBudgetPerPersonException('Number Of Travellers Cannot be Less Than 1')