from Vehicles.Electric_transport.Electric_transport import ElectricTransport


class Tram(ElectricTransport):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price,
                 electricity_needed_per_hour_in_watts):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price,
                         electricity_needed_per_hour_in_watts)

    def __str__(self):
        return f'Vehicle type: {self.vehicles_type}, vehicle capacity of people: {self.vehicles_capacity_of_people}, ' \
               f'vehicle price: {self.vehicles_price}, ' \
               f'electricity needed per hour in watts: {self.electricity_needed_per_hour_in_watts}'
