from all_airporst import All_Airports
from airlines import Airlines
from trip import Trip
from itertools import permutations
class Travel_Agent:
      def __init__(self,name) -> None:
            self.name =name
            self.trip =None
            self.all_airports=All_Airports()
            self.air_lines =Airlines()
            
      
      def set_trip_one_city_one_way(self,start,end,start_date):
            price =self.all_airports.ticket_price(start,end)
            distance = self.all_airports.two_airports_distance(start,end)
            aircraft =self.air_lines.get_aircraft_by_distance(distance)
            trip =Trip([start,end],aircraft,price,start_date,route=[start,end])
            return trip
      
      def set_trip_two_city_round_way(self,start,end,start_date):
            trip_1 = self.set_trip_one_city_one_way(start,end,start_date)
            trip_2 = self.set_trip_one_city_one_way(end,start,start_date)
            return [trip_1,trip_2]
      
      
      def set_trip_two_city_one_way(self,trip_info,start_date):
            trip_1 = self.set_trip_one_city_one_way(trip_info[0],trip_info[1],start_date)
            trip_2 = self.set_trip_one_city_one_way(trip_info[1],trip_info[2],start_date)
            return [trip_1,trip_2]
      
      def set_trip_multi_city_one_wayz_fixed_route(self,tripe_info,start_date):
            trips =[]
            for i in range(0,len(tripe_info)-1):
                  trip= self.set_trip_one_city_one_way(tripe_info[i],tripe_info[i+1],start_date)
                  trips.append(trip)
            return trips
      
      def set_trip_multi_city_one_wayz_flexible_route(self,tripe_cities,start_date):
            
            start_city = tripe_cities[0]
            flexible_cities=tripe_cities[1:]
            min_price =float("inf")
            selected_trips =None
            for sequence in permutations(flexible_cities):
                  
                  cities =[start_city] + list(sequence)
                  fixed_route_trips = self.set_trip_multi_city_one_wayz_fixed_route(cities,start_date)
                  price =0
                  for trip in fixed_route_trips:
                        price +=trip.price
                  if price <min_price:
                        min_price =price
                        selected_trips= fixed_route_trips
            
            return selected_trips,min_price
      
      
      def set_trip_multi_city_two_way(self):
            pass
      
      def __repr__(self) -> str:
            return f"Travel agent {self.name}"

      