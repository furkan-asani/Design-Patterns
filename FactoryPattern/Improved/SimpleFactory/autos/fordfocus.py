from .abs_auto import AbsAuto


class FordFocus(AbsAuto):
    def start(self):
        print("Ford Focus running smoothly!")

    def stop(self):
        print("Ford Focus has been turned off.")
