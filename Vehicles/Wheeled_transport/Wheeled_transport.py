from Vehicles.Vehicles import Vehicles


class Wheeled_transport(Vehicles):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, amount_of_wheels):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price)
        self.amount_of_wheels = amount_of_wheels