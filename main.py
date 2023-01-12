from travel_agent import Travel_Agent
def main():
      travel_agent= Travel_Agent("kesto agent")
      trip_info=travel_agent.set_trip_one_city_one_way("DAC","PRA","11/7/2022")
      # print(trip_info.aircraft)
      # print(trip_info.price)

      trip_cities=["DUB","LHR","SYD","JFK"]
      trip_info=travel_agent.set_trip_multi_city_one_wayz_flexible_route(trip_cities,"11/7/2022")
      print(trip_info[1])
      for i in trip_info[0]:
            print(i)
      
if __name__ == "__main__":
      main()