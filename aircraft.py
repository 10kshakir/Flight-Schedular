class Aircraft:
      def __init__(self,company,code,type,flight_range) -> None:
            self.made_by=company
            self.code =code
            self.type =type
            self.flight_range=float(flight_range)
      
      def get_maker_of_plane(self):
            return self.made_by
      
      def get_flight_range(self):
            return self.flight_range
      def __repr__(self) -> str:
            return f"AirCraft code {self.code} type {self.type} flight range {self.flight_range}  made by {self.made_by}"
      