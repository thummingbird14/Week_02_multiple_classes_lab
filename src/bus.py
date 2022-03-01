class Bus:

    def __init__(self, route_num, destination):
        self.route_number = route_num
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)
    
        