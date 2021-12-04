from .abs_auto import AbsAuto


class FordFocus(AbsAuto):
    def start(self):
        print("%s running smoothly!" % self.name)

    def stop(self):
        print("%s has been turned off." % self.name)
