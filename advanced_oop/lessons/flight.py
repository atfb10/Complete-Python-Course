'''
Flight Leg:
GLA -> LHR -> CAN

2 segments (GLA -> LHR, LHR -> CAN)
'''

from typing import List

class Segment:
    def __init__(self, departure: str, destination: str):
        self.departure = departure
        self.destination = destination

class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments
    
    def __len__(self):
        return len(self.segments)
    
    def __getitem__(self, i):
        return self.segments[i]
    
    def __repr__(self) -> str:
        flight_itinery = f'{self.segments[0].departure} -> {self.segments[0].destination}'
        total_stops = len(self.segments) - 1
        for i in range(1, total_stops):
            flight_itinerary += f' -> {self.segments[i].departure} -> {self.segments[i].destination}'
        return flight_itinery
            

    # Getter
    @property
    def departure_point(self) -> str:
        return self.segments[0].departure
    
    # Setter
    @departure_point.setter
    def departure_point(self, value: str) -> None:
        self.segments[0] = Segment(value, self.segments[0].destination)
        return

    @property
    def landing_point(self) -> str:
        return self.segments[len(self.segments) - 1].destination

    @landing_point.setter
    def landing_point(self, value: str) -> None:
        self.segments[len(self.segments) - 1] = Segment(self.segments[len(self.segments) - 1].departure, value)
        return

flight_seg = Segment('GLA', 'LHR')
my_flight = Flight(flight_seg)
print(my_flight)

my_flight.departure_point = 'EDI'
print(my_flight)