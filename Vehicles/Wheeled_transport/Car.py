from Vehicles.Wheeled_transport.Wheeled_transport import WheeledTransport


class Car(WheeledTransport):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, fuel_capacity_in_liters):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price,fuel_capacity_in_liters)

    def __str__(self):
        return f'Vehicle type: {self.vehicles_type}, vehicle capacity of people: {self.vehicles_capacity_of_people}, ' \
               f'vehicle price: {self.vehicles_price}, fuel capacity in liters: {self.fuel_capacity_in_liters}'