from django.http import JsonResponse
from main.models import Neighborhood

def neighborhoods_by_city(request):
    city_id = request.GET.get('city_id')
    if not city_id:
        return JsonResponse({'error': 'city_id required'}, status=400)
    neighborhoods = Neighborhood.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse({'neighborhoods': list(neighborhoods)})
