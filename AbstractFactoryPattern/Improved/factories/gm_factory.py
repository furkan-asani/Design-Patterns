from factories.abs_factory import AbstractFactory
from autos.gm.chevy_spark import ChevySpark
from autos.gm.chevy_camaro import ChevyCamaro
from autos.gm.cadillac import CadillacCTS


class GMFactory(AbstractFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
