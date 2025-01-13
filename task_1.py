from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make: str = make
        self.model: str = model
        self.region: str = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        print(f"{self.make} {self.model} {self.region}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        print(f"{self.make} {self.model} {self.region}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self) -> None:
        self.region: str = "US Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.region)


class EUVehicleFactory(VehicleFactory):
    def __init__(self) -> None:
        self.region: str = "EU Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.region)


if __name__ == "__main__":
    us_vehicle_factory = USVehicleFactory()
    eu_vehicle_factory = EUVehicleFactory()

    vehicle1 = us_vehicle_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_vehicle_factory.create_car("Audi", "A4")
    vehicle2.start_engine()

    vehicle3 = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Street Glide")
    vehicle3.start_engine()

    vehicle4 = eu_vehicle_factory.create_motorcycle("BMW", "R1250GS")
    vehicle4.start_engine()
