from autos.abs_auto import AbstractAuto


class ChevyCamaro(AbstractAuto):
    def start(self):
        print("Chevy Camaro running smoothly")

    def stop(self):
        print("Chevy Camaro shutting down")
