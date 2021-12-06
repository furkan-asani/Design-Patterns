from autos.abs_auto import AbstractAuto


class FordFiesta(AbstractAuto):
    def start(self):
        print("Ford Fiesta running smoothly")

    def stop(self):
        print("Ford Fiesta shutting down")
