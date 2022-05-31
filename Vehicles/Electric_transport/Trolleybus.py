from python_lab9.Vehicles.Electric_transport.Electric_transport import Electric_transport


class Trolleybus(Electric_transport):
    def __init__(self, vehicles_type, vehicles_capacity_of_people, vehicles_price, electricity_needed_per_hour):
        super().__init__(vehicles_type, vehicles_capacity_of_people, vehicles_price,electricity_needed_per_hour)

    def __str__(self):
        return f'Vehicle type: {self.vehicles_type}, vehicle capacity of people: {self.vehicles_capacity_of_people}, ' \
               f'vehicle price: {self.vehicles_price}, electricity needed per hour: {self.electricity_needed_per_hour}'