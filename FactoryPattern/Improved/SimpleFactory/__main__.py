from autofactory import AutoFactory

factory = AutoFactory()

for carName in 'ChevyVolt', 'FordFocus', 'JeepSahara', 'Tesla P980D':
    car = factory.createInstance(carName)
    car.start()
    car.stop()