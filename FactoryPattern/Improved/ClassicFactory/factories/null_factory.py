from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullCarFactory(AbsFactory):
    def create_auto(self):
        self.nullCar = nullCar = NullCar("Unknown")
        nullCar.name = "Unknown"
        return nullCar
