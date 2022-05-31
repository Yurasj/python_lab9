from Vehicles.Wheeled_transport.Wheeled_transport import Wheeled_transport


class Car(Wheeled_transport):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, amount_of_wheels):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price,amount_of_wheels)

    def __str__(self):
        return f'Vehicle type: {self.vehicles_type}, vehicle capacity of people: {self.vehicles_capacity_of_people}, ' \
               f'vehicle price: {self.vehicles_price}, amount of wheels: {self.amount_of_wheels}'