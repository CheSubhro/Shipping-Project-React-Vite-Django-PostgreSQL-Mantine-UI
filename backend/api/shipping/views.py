
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShippingRate

class CalculateShippingView(APIView):
    
    def get_lat_lon(self, city_name):
        url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
        headers = {
            'User-Agent': 'MyShippingApp_v1_Contact_chesub' 
        }
        
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                if len(data) > 0:
                    lat = data[0]['lat']
                    lng = data[0]['lon']
                    return float(lat), float(lng)
                else:
                    print(f"City '{city_name}' not found.")
            else:
                print(f"Server Error: {res.status_code}")
        except Exception as e:
            print(f"Geocoding Error: {e}")
            
        return None, None
        
    def get_road_distance(self, lat1, lon1, lat2, lon2):
        url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false"
        try:
            response = requests.get(url).json()
            if response.get('routes'):
                return response['routes'][0]['distance'] / 1000
        except Exception as e:
            print(f"OSRM Error: {e}")
        return None

    def post(self, request):
        source = request.data.get('source_city')
        destination = request.data.get('destination_city')
        weight = float(request.data.get('weight_kg', 0))

        s_lat, s_lon = self.get_lat_lon(source)
        d_lat, d_lon = self.get_lat_lon(destination)

        if s_lat is None or d_lat is None:
            return Response({"error": "One or both cities not found!"}, status=status.HTTP_400_BAD_REQUEST)

        distance_km = self.get_road_distance(s_lat, s_lon, d_lat, d_lon)

        if distance_km is None:
            return Response({"error": "Could not calculate distance!"}, status=status.HTTP_400_BAD_REQUEST)

        base_price = 50
        distance_cost = max(0, distance_km - 10) * 5
        weight_cost = weight * 10
        total_cost = base_price + distance_cost + weight_cost

        ShippingRate.objects.create(
            source_city=source,
            destination_city=destination,
            distance_km=round(distance_km, 2),
            weight_kg=weight,
            total_cost=round(total_cost, 2)
        )

        return Response({
            "status": "success",
            "distance": f"{round(distance_km, 2)} km",
            "total_cost": f"₹{round(total_cost, 2)}",
            "breakdown": {
                "base": base_price,
                "distance_charge": round(distance_cost, 2),
                "weight_charge": weight_cost
            }
        }, status=status.HTTP_200_OK)