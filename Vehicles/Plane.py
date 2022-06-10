from Vehicles.Vehicles import Vehicles


class Plane(Vehicles) :
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, type_of_landing) -> None:
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price)
        self.type_of_landing = type_of_landing

    def __str__(self) -> str:
        return f'Vehicle type: {self.vehicles_type}, vehicle capacity of people: {self.vehicles_capacity_of_people}, ' \
               f'vehicle price: {self.vehicles_price}, type of landing: {self.type_of_landing}'