from Vehicles.Vehicles import Vehicles


class ElectricTransport(Vehicles):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, electricity_needed_per_hour_in_watts) -> None:
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price)
        self.electricity_needed_per_hour_in_watts = electricity_needed_per_hour_in_watts
