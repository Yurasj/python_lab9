from Vehicles.Vehicles import Vehicles


class WheeledTransport(Vehicles):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, fuel_capacity_in_liters) -> None:
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price)
        self.fuel_capacity_in_liters = fuel_capacity_in_liters
