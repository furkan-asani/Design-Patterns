from autos.abs_auto import AbstractAuto


class CadillacCTS(AbstractAuto):
    def start(self):
        print("CadillacCTS running smoothly")

    def stop(self):
        print("CadillacCTS shutting down")
