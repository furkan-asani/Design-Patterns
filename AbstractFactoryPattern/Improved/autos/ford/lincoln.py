from autos.abs_auto import AbstractAuto


class LincolnMKS(AbstractAuto):
    def start(self):
        print("LincolnMKS running smoothly")

    def stop(self):
        print("LincolnMKS shutting down")
