from autos.abs_auto import AbstractAuto


class ChevySpark(AbstractAuto):
    def start(self):
        print("Chevy Spark running smoothly")

    def stop(self):
        print("Chevy Spark shutting down")
