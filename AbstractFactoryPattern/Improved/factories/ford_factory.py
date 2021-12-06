from factories.abs_factory import AbstractFactory
from autos.ford.ford_fiesta import FordFiesta
from autos.ford.ford_mustang import FordMustang
from autos.ford.lincoln import LincolnMKS


class FordFactory(AbstractFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
