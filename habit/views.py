# In your Django app's views.py module
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .food_recommendation_v1 import food_recommendation
import json

@csrf_exempt
def recommend_food(request):
    if request.method == 'POST':
        # Assume JSON data with a list of food items is sent in the request body
        data = json.loads(request.body.decode('utf-8'))
        
        input_food_list = []
        for food_item in data['userlogs']:
            category_code = food_item['categoryCode']
            name = food_item['name']
            category = food_item['category']
            input_food_list.append([category_code, name, category])
        
        # Call the method from your integrated script
        recommended_foods = food_recommendation.run_food_recommandation(input_food_list,food_recommendation)

        # Serialize the recommended foods (if necessary)
        # Here, you might want to convert the DataFrame to a JSON object
        serialized_data = recommended_foods

        # Return the serialized data as an HTTP response
        return JsonResponse(serialized_data, safe=False)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
