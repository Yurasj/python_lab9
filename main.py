from Vehicles.Plane import Plane
from Vehicles.ElectricTransport.Tram import Tram
from Vehicles.ElectricTransport.Trolleybus import Trolleybus
from Vehicles.WheeledTransport.Car import Car
from Vehicles.WheeledTransport.Bus import Bus


def main() -> None:
    plane = Plane('plane', 100, 6700000, 'ground')
    tram = Tram('tram', 40, 430000, 140)
    trolleybus = Trolleybus('trolleybus', 27, 310000, 113)
    car = Car('car', 5, 278000, 4)
    bus = Bus('bus', 24, 324000, 4)
    print(plane)
    print(tram)
    print(trolleybus)
    print(car)
    print(bus)


if __name__ == '__main__':
    main()
