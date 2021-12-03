from .abs_auto import AbsAuto

class ChevyVolt(AbsAuto):
    def start(self):
        print("Chevy Volt running with shocking power!")

    def stop(self):
        print("Chevy Volt shutting down.")
