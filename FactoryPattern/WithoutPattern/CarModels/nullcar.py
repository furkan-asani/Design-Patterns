class NullCar(object):
    def __init__(self, carName):
        self._carName = carName

    def start(self):
        print('Unknown car "%s."' % self._carName)

    def stop(self):
        pass