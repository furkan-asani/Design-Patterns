from autos.abs_auto import AbstractAuto


class FordMustang(AbstractAuto):
    def start(self):
        print("Ford Mustang running smoothly")

    def stop(self):
        print("Ford Mustang shutting down")
