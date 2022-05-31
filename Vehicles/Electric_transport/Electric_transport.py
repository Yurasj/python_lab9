from Vehicles.Vehicles import Vehicles


class Electric_transport(Vehicles):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, electricity_needed_per_hour):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price)
        self.electricity_needed_per_hour = electricity_needed_per_hour