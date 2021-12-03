from inspect import getmembers, isclass, isabstract
import autos


class AutoFactory(object):
    autos = {}

    def __init__(self):
        self.loadAutos()

    def loadAutos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update([[name, _type]])

    def createInstance(self, carName):
        if carName in self.autos:
            return self.autos[carName]()
        else:
            return autos.NullCar(carName)
