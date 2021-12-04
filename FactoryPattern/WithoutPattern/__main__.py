from CarModels.chevyvolt import ChevyVolt
from CarModels.fordfocus import FordFocus
from CarModels.jeepsahara import JeepSahara
from CarModels.nullcar import NullCar

def getCar(carName):
    if carName == 'Chevy':
        return ChevyVolt()
    elif carName == 'Ford':
        return FordFocus()
    elif carName == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carName)

for carName in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = getCar(carName)
    car.start()
    car.stop()
    