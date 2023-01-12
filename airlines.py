import csv
from aircraft import Aircraft
class Airlines:
      def __init__(self) -> None:
            self.air_craft=None
            self.load_air_craft_data("aircraft.csv")
      
      def load_air_craft_data(self,csv_file):
            air_crafts={}
            with open(csv_file,"r" )as file:
                  lines =csv.reader(file)
                  next(lines)
                  for line in lines:
                        air_crafts[line[0]] =Aircraft(line[3],line[0],line[1],line[4])
            file.close()
            self.air_craft =air_crafts
            # for air_craft in air_crafts.items():
            #       print(air_craft)           

      def get_aircraft_code(self,aircraft_code):
            return self.air_craft[aircraft_code]
      
      def get_aircraft_by_distance(self,distance):
            for aircraft in self.air_craft.values():
                  if aircraft.flight_range <distance:
                        return aircraft
            
      
