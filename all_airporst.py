import csv
from airport import Airport
from math import radians,sin,cos,atan2,sqrt
class All_Airports:
      def __init__(self) -> None:
            self.airports=None
            self.load_airport_data("airport.csv")
      
      def load_airport_data(self,file_path):
            airport ={}
            currency_rates={}
            country_currency={}
            # get currency rates
            with open ("currencyrates.csv","r",encoding="utf-8")as file:
                  lines =csv.reader(file)
                  for line in lines:
                        currency_rates[line[1]]=line[2]
            file.close()
                  
             #country currency name
            with open("countrycurrency.csv","r",encoding="utf-8")as file:
                  lines=csv.reader(file)
                  for line in lines:
                        country_currency[line[0]]=line[1]
            file.close()
                  
             
              
            with open(file_path,"r",encoding="utf-8") as file:
                  lines =csv.reader(file)
                  try:
                        for line in lines:
                              country =line[3]
                              if country not in country_currency:
                                    continue
                              currency =country_currency[country]
                              if currency not in currency_rates:
                                    continue
                              rate = currency_rates[currency]
                              
                              airport[line[4]]=Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
                  except KeyError as e:
                        print("key not found",e)
                        
            file.close()
            self.airports=airport
            # for airport in self.airports.items():
            #       print(airport)
      
      def get_distance_between_two_airports(self,lat1,lon1,lat2,lon2):
            earth_radians =6371
            
            dlat=radians(lat1 -lat2)
            dlon=radians(lon1 -lon2)
            a = (sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2))
            c = 2 * atan2(sqrt(a),sqrt(1 - a))
            d = earth_radians * c
            return d
      
      def two_airports_distance(self,airport1_code,airport2_code):
            airport1 =self.airports[airport1_code]
            airport2 =self.airports[airport2_code]
            
            distance =self.get_distance_between_two_airports(airport1.lat,airport1.lon,airport2.lat,airport2.lon)
            return distance
      
      def ticket_price(self,start,end):
            distance =self.two_airports_distance(start,end)
            airport_1= self.airports[start]
      
            fare = distance *airport_1.rate
            return fare      
      
      
world_tour =All_Airports()
fare =world_tour.ticket_price("DAC","PRA")  
